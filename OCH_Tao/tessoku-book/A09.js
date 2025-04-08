const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [H, W, N] = input.shift().split(" ").map(x => parseInt(x, 10));
let X = Array(H + 9).fill([]).map(_ => Array(W + 9).fill(0));
for (const i of input) {
  const [A, B, C, D] = i.split(" ").map(x => parseInt(x, 10));
  X[A][B]++;
  X[C + 1][D + 1]++;
  X[A][D + 1]--;
  X[C + 1][B]--;
}
for (let i = 1; i < H + 1; i++) {
  for (let j = 1; j < W + 1; j++) {
    X[i][j] += X[i][j - 1];
  }
}
for (let i = 1; i < W + 1; i++) {
  for (let j = 1; j < H + 1; j++) {
    X[j][i] += X[j - 1][i];
  }
}
for (let i = 1; i < H + 1; i++) {
  console.log(...X[i].slice(1, W + 1));
}