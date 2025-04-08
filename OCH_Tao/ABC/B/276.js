const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, M] = input.shift().split(" ").map(x => parseInt(x, 10));
let X = new Array(N).fill(0).map(x => new Set());
for (let i = 0; i < M; i++) {
  const [A, B] = input[i].split(" ").map(x => parseInt(x, 10));
  X[A - 1].add(B);
  X[B - 1].add(A);
}
for (const i of X) {
  console.log(i.size, ...[...i].sort((a, b) => a - b));
}