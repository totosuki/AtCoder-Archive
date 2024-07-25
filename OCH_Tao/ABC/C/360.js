const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
const W = input[2].split(" ").map(x => parseInt(x, 10));
let L = new Array(N).fill(0);
for (let i = 0; i < N; i++) {
  L[A[i] - 1] = Math.max(L[A[i] - 1], W[i]);
}
console.log(W.reduce((a, b) => a + b, 0) - L.reduce((a, b) => a + b, 0));