input = `
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
`;

input = `
2222
`;

input = `
1191
9111
`;

function parsInput() {
  const board = [];
  input.split("\n").forEach((line) => {
    if (line.length === 0) return;
    board.push(line.split("").map((c) => Number(c)));
  });
  return board;
}

const board = parsInput();

const inBounds = (r, c) => {
  return r >= 0 && c >= 0 && r < board.length && c < board[0].length;
};

const openList = [
  {
    r: 0,
    c: 0,
    stepsInDirection: 0,
    accumulatedHeatLoss: 0,
    prevDirection: undefined,
  },
];
const maxStepsInDirection = 3;
const seen = new Set(["0,0"]);
while (openList.length) {
  openList.sort((a, b) => a.heatLoss - b.heatLoss);
  const node = openList.shift();
  console.log("node", node);
  const neighbors = {
    up: { r: node.r - 1, c: node.c },
    down: { r: node.r + 1, c: node.c },
    left: { r: node.r, c: node.c - 1 },
    right: { r: node.r, c: node.c + 1 },
  };
  for (const direction in neighbors) {
    const neighbor = neighbors[direction];
    const childKey = `${neighbor.c},${neighbor.r}`;
    if (seen.has(childKey)) continue;
    seen.add(childKey);
    if (!inBounds(neighbor.r, neighbor.c)) continue;
    const heatLoss = board[neighbor.r][neighbor.c];

    const child = {
      ...neighbor,
      prevDirection: direction,
      accumulatedHeatLoss: node.accumulatedHeatLoss + heatLoss,
      stepsInDirection:
        node.prevDirection === neighbor ? node.stepsInDirection + 1 : 1,
    };
    if (child.stepsInDirection > maxStepsInDirection) continue;
    openList.push(child);
    if (child.r === board.length - 1 && child.c === board[0].length - 1) {
      console.log(child.accumulatedHeatLoss);
      return;
    }
  }
}
