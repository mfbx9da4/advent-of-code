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
input = `
%ls -> gl
%rz -> vm, gl
broadcaster -> rz, fp, kv, fd
%ql -> bn
%bm -> hr, fj
%fp -> cc, gk
&lk -> nc
%xg -> gl, mz
%dg -> gk, mp
%zg -> ls, gl
%lg -> hr
%pt -> lg, hr
%sp -> mj
%ms -> gl, hx
%kj -> fl, gk
%bn -> rj, gk
%xc -> vq
%fl -> gk
%dh -> hr, nm
%jk -> gk, dg
%tf -> cb
%kd -> cm, nr
&hr -> hh, kv, xl, qq
%kv -> xr, hr
%hq -> ql
&fn -> nc
%vm -> gl, xn
%jh -> nr, kd
%mz -> dd
%tp -> hq
%cf -> nr
%gr -> jh
%jd -> hr, bm
%xr -> qq, hr
%cm -> nr, cf
&fh -> nc
%rb -> xl, hr
&nc -> rx
%mp -> gk, kj
&nr -> fd, gr, fn, cb, tf, xc, vq
&gl -> fh, xn, sp, mz, rz, mj, dd
%rj -> jk
&hh -> nc
%fd -> nr, df
&gk -> lk, tp, fp, ql, hq, rj
%fj -> pt, hr
%qq -> dh
%df -> nr, nv
%mj -> ms
%xn -> xg
%cc -> gk, tp
%nm -> rb, hr
%dd -> sp
%vq -> gr
%cb -> xc
%nv -> tf, nr
%xl -> jd
%hx -> gl, zg
`;

// // Example 1
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

// Plan:
// 1. Construct the graph
// 2. Run BFS keeping track of number of high and low pulses
// 3. If we need to find the cycle and multiply it out for 1000 times

type Pulse = "low" | "high";

type BaseModule = {
  name: string;
  output: Pulse;
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
  inputs: Map<Module, Pulse>;
};
type FlipFlopModule = BaseModule & {
  type: "%";
  state: Pulse;
};
type Module =
  | ButtonModule
  | OutputModule
  | BroadcasterModule
  | ConjunctionModule
  | FlipFlopModule;

type Graph = Map<Module, Array<Module>>;

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

  const nameToModule: Map<string, Module> = new Map([
    ["output", { type: "output", name: "output", output: "low" }],
    ["rx", { type: "output", name: "rx", output: "low" }],
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
        state: "low",
        get output() {
          return this.state;
        },
      };
    } else {
      module = { type, name, output: "low" };
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

type WorkingModule = {
  module: Module;
  output: Pulse;
};

let lowCount = 0;
let highCount = 0;

function pressButton() {
  const openList: Array<Module> = [buttonModule];
  while (openList.length > 0) {
    const module = openList.shift()!;
    const signal = module.output;
    for (const child of graph.get(module) ?? []) {
      assert(child.type !== "button", "button should not be in graph");
      if (signal === "low") lowCount++;
      else highCount++;
      if (child.type === "%" && signal === "low") {
        child.state = child.state === "high" ? "low" : "high";
        openList.push(child);
      } else if (child.type === "&") {
        child.inputs.set(module, signal);
        openList.push(child);
      } else if (child.type === "broadcaster") {
        openList.push(child);
      } else if (child.type === "output") {
        console.log("Output", signal);
      }
    }
  }
}

for (let i = 0; i < 1000; i++) pressButton();
console.log("lowCount", lowCount);
console.log("highCount", highCount);
console.log("lowCount * highCount", lowCount * highCount);
