const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [H, W] = input[0].split(" ").map(x => parseInt(x, 10));
let X = Array(H + 1).fill([]).map(_ => Array(W + 1).fill(0));
for (let i = 1; i < H + 1; i++) {
  const Y = input[i].split(" ").map(x => parseInt(x, 10));
  for (let j = 1; j < W + 1; j++) {
    X[i][j] = Y[j - 1] + X[i][j - 1];
  }
}
for (let i = 1; i < W + 1; i++) {
  for (let j = 1; j < H + 1; j++) {
    X[j][i] += X[j - 1][i];
  }
}
const Q = parseInt(input[H + 1], 10);
for (let i = H + 2; i < H + Q + 2; i++) {
  const [A, B, C, D] = input[i].split(" ").map(x => parseInt(x, 10));
  console.log(X[C][D] + X[A - 1][B - 1] - X[C][B - 1] - X[A - 1][D]);
}