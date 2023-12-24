import { graphvizVersion } from "@viz-js/viz";
import * as Viz from "@viz-js/viz";

let input: string = "";
// David's Input
input = `
%jf -> cr, dn
%fd -> hm, jx
%mb -> bq, cr
&mr -> qt
%qd -> cr, dg
%rs -> hh
%xl -> gq, vj
%zl -> qn
%tj -> cr, qd
%fn -> hn
%qc -> tf
%fh -> jj, vj
&kk -> qt
%qn -> jx, fn
%hm -> jx, fq
%cm -> vj, fh
%jj -> vj, lp
%dr -> vj, qc
broadcaster -> db, hd, cm, xf
%fq -> jx, zk
%hd -> jx, zl
&qt -> rx
&vj -> bb, qc, cm
%tt -> bd
%sf -> jx
%rg -> nl, hr
%zk -> jx, sf
%lp -> cz, vj
%xf -> mb, cr
&cr -> dg, bq, kk, xf, gm
%nb -> vj, dr
%dg -> vm
%ql -> nl
&gl -> qt
&nl -> db, hr, mr, hh, hk, rs, bn
%ff -> ql, nl
%rb -> cr
%lc -> vj
%vm -> gm, cr
%tf -> vj, xl
%hr -> kf
%kf -> xx, nl
&bb -> qt
%ml -> nl, bn
%bq -> tj
%db -> ml, nl
%hn -> jx, tt
%dn -> cr, rb
%gm -> qs
%gq -> lc, vj
%hh -> rg
%bd -> fd
%xx -> nl, ff
%qs -> jf, cr
&jx -> fn, bd, tt, gl, zl, hd
%cz -> nb, vj
%bn -> hk
%hk -> rs
`;

// Leandro’s input
// input = `
// %ls -> gl
// %rz -> vm, gl
// broadcaster -> rz, fp, kv, fd
// %ql -> bn
// %bm -> hr, fj
// %fp -> cc, gk
// &lk -> nc
// %xg -> gl, mz
// %dg -> gk, mp
// %zg -> ls, gl
// %lg -> hr
// %pt -> lg, hr
// %sp -> mj
// %ms -> gl, hx
// %kj -> fl, gk
// %bn -> rj, gk
// %xc -> vq
// %fl -> gk
// %dh -> hr, nm
// %jk -> gk, dg
// %tf -> cb
// %kd -> cm, nr
// &hr -> hh, kv, xl, qq
// %kv -> xr, hr
// %hq -> ql
// &fn -> nc
// %vm -> gl, xn
// %jh -> nr, kd
// %mz -> dd
// %tp -> hq
// %cf -> nr
// %gr -> jh
// %jd -> hr, bm
// %xr -> qq, hr
// %cm -> nr, cf
// &fh -> nc
// %rb -> xl, hr
// &nc -> rx
// %mp -> gk, kj
// &nr -> fd, gr, fn, cb, tf, xc, vq
// &gl -> fh, xn, sp, mz, rz, mj, dd
// %rj -> jk
// &hh -> nc
// %fd -> nr, df
// &gk -> lk, tp, fp, ql, hq, rj
// %fj -> pt, hr
// %qq -> dh
// %df -> nr, nv
// %mj -> ms
// %xn -> xg
// %cc -> gk, tp
// %nm -> rb, hr
// %dd -> sp
// %vq -> gr
// %cb -> xc
// %nv -> tf, nr
// %xl -> jd
// %hx -> gl, zg
// `;

// Example 1
// input = `
// broadcaster -> a, b, c
// %a -> b
// %b -> c
// %c -> inv
// &inv -> a
// `;

// // Example 2
// input = `
// broadcaster -> a
// %a -> inv, con
// &inv -> b
// %b -> con
// &con -> output
// `;

// An example which has 10 chained flip flops
input = `
broadcaster -> a
%a -> b
%b -> c
%c -> d
%d -> e
&e -> f, a
%f -> g
%g -> h
%h -> i
%i -> j
%j -> con
&con -> output
`;
input = `
broadcaster -> a
%a -> b
%b -> c
%c -> d
%d -> e
%e -> con
&con -> output
`;

// Plan:
// 1. Construct the graph
// 2. Run BFS keeping track of number of high and low pulses
// 3. If we need to find the cycle and multiply it out for 1000 times

type Pulse = "low" | "high";

type BaseModule = {
  name: string;
  output: Pulse | undefined;
};

type ButtonModule = BaseModule & {
  type: "button";
};
type OutputModule = BaseModule & {
  type: "output";
};
type BroadcasterModule = BaseModule & {
  type: "broadcaster";
};
type ConjunctionModule = BaseModule & {
  type: "&";
  inputs: Map<Module, Pulse | undefined>;
};
type FlipFlopModule = BaseModule & {
  type: "%";
  state: Pulse;
  runId: number | undefined;
};
type Module =
  | ButtonModule
  | OutputModule
  | BroadcasterModule
  | ConjunctionModule
  | FlipFlopModule;

type Graph = Map<Module, Array<Module>> & { runId?: number };

function assert(condition: any, msg: string): asserts condition {
  if (!condition) {
    throw new Error(`Assertion failed ${msg ?? ""}`);
  }
}

function parseInput(input: string): { graph: Graph; buttonModule: Module } {
  const lines = input
    .trim()
    .split("\n")
    .filter((line) => line.length > 0);
  const graph: Graph = new Map();
  graph.runId = 0;

  const output: OutputModule = {
    type: "output",
    name: "output",
    output: undefined,
  };
  const rx: OutputModule = { type: "output", name: "rx", output: undefined };
  const nameToModule: Map<string, Module> = new Map([
    ["output", output],
    ["rx", rx],
  ]);
  for (const line of lines) {
    // console.log(line);
    const [from, to] = line.split("->").map((s) => s.trim());
    const type = from[0] === "&" ? "&" : from[0] === "%" ? "%" : "broadcaster";
    const name = from.replace(/%|&/g, "").trim();
    let module: Module;
    if (type === "&") {
      module = {
        type,
        name,
        inputs: new Map(),
        get output() {
          return [...this.inputs.values()].every((x) => x === "high")
            ? "low"
            : "high";
        },
      };
    } else if (type === "%") {
      module = {
        type,
        name,
        runId: undefined,
        state: "low",
        get output() {
          return this.runId === graph.runId ? this.state : undefined;
        },
      };
    } else if (type === "broadcaster" || type === "button") {
      module = { type, name, output: "low" };
    } else {
      throw new Error(`Unknown type ${type}`);
    }
    graph.set(module, []);
    nameToModule.set(name, module);
  }
  const broadcaster = nameToModule.get("broadcaster");
  assert(broadcaster, "broadcaster not found in nameToModule map");
  const buttonModule: ButtonModule = {
    type: "button",
    name: "button",
    output: "low",
  };
  graph.set(buttonModule, [broadcaster]);

  for (const line of lines) {
    const [from, to] = line.split("->").map((s) => s.trim());
    const name = from.replace(/%|&/g, "").trim();
    const fromModule = nameToModule.get(name)!;
    const toModules = to.split(",").map((s) => s.trim());
    for (const toModule of toModules) {
      const toName = toModule.replace(/%|&/g, "").trim();
      const toModuleObj = nameToModule.get(toName);
      assert(toModuleObj, `toModuleObj not found for ${toName}`);
      if (toModuleObj.type === "output") graph.set(toModuleObj, []);
      graph.get(fromModule)!.push(toModuleObj);
      if (toModuleObj.type === "&") {
        toModuleObj.inputs.set(fromModule, "low");
      }
    }
  }

  return { graph, buttonModule };
}

const { graph, buttonModule } = parseInput(input);
// console.log("graph", graph);

let lowCount = 0;
let highCount = 0;

async function pressButton(): Promise<boolean> {
  console.log("pressButton");
  const openList: Array<Module> = [buttonModule];
  graph.runId = (graph.runId ?? 0) + 1;
  while (openList.length > 0) {
    const module = openList.shift()!;
    console.log("module", module.name, module.output);
    const signal = module.output;
    // d3Drawing.update(graph, module.name);
    // await new Promise((r) => setTimeout(r, 1000));
    assert(signal !== undefined, "signal should not be undefined");
    for (const child of graph.get(module) ?? []) {
      assert(child.type !== "button", "button should not be in graph");
      if (signal === "low") lowCount++;
      else highCount++;
      if (child.type === "%") {
        if (signal === "low") {
          child.runId = graph.runId;
          child.state = child.state === "high" ? "low" : "high";
          openList.push(child);
        }
      } else if (child.type === "&") {
        child.inputs.set(module, signal);
        openList.push(child);
      } else if (child.type === "broadcaster") {
        openList.push(child);
      } else if (child.type === "output" && signal === "low") {
        return true;
      }
    }
  }

  return false;
}

function drawGraphUsingViz(viz: Viz.Viz) {
  const graphToData = (graph: Graph, activeModuleName?: string) => {
    const typeToShape = {
      button: "hexagon",
      broadcaster: "hexagon",
      output: "hexagon",
      "&": "circle",
      "%": "square",
    };

    const outputToColor = {
      low: "crimson",
      high: "forestgreen",
      undefined: "grey",
    };
    const nodes: Viz.Graph["nodes"] = [...graph.keys()].map((module) => {
      const node = {
        id: module.name,
        name: module.name,
        attributes: {
          color: "black",
          shape: typeToShape[module.type],
          fontname: "Courier",
          fontcolor: "white",
          fillcolor:
            module.type === "output" || module.type === "button"
              ? "dodgerblue"
              : module.type === "%"
              ? module.state === "low"
                ? "crimson"
                : "forestgreen"
              : outputToColor[String(module.output)],
          style: "filled",
          class: module.name === activeModuleName ? "active" : "",
          root: module.name === "button",
        },
      };
      return node;
    });
    const edges: Viz.Graph["edges"] = [...graph.entries()].flatMap(
      ([from, tos]) => {
        return tos.map((to) => {
          const color = outputToColor[String(from.output)];
          return {
            tail: from.name,
            head: to.name,
            attributes: {
              fillcolor: color,
              color,
              penwidth: 5,
            },
          };
        });
      }
    );
    return { nodes, edges };
  };

  const data = graphToData(graph);
  let svg = viz.renderSVGElement(data);
  document.body.appendChild(svg);

  return {
    update: (graph: Graph, activeModuleName?: string) => {
      svg.remove();
      const data = graphToData(graph, activeModuleName);
      svg = viz.renderSVGElement(data);
      document.body.appendChild(svg);
    },
  };
}

let d3Drawing: ReturnType<typeof drawGraphUsingViz>;

const main = async () => {
  const viz = await import("@viz-js/viz").then((module) => module.instance());

  d3Drawing = drawGraphUsingViz(viz);

  for (let i = 0; i < Infinity; i++) {
    if (i % 10000000 === 0) {
      console.log("i", i);
    }

    if (i % 1000 === 0 && i > 0) {
      console.log("draw", i, lowCount * highCount);
      // console.log("low * high", lowCount * highCount);
      d3Drawing.update(graph);
      await new Promise((resolve) => setTimeout(resolve, 100));
    }

    d3Drawing.update(graph);
    await new Promise((resolve) => setTimeout(resolve, 1000));

    if (await pressButton()) {
      // TODO: REENABLE
      console.log("------- i", i);
      d3Drawing.update(graph);
      break;
    }

    // if (i > 2000) break;
  }
};

const startButton = document.createElement("button");
startButton.innerText = "Start";
startButton.onclick = main;
document.body.appendChild(startButton);
main();
