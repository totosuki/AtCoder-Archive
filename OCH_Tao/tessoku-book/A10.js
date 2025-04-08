const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift(), 10);
const A = input.shift().split(" ").map(x => parseInt(x, 10));
let P = Array(100009).fill(0);
let Q = Array(100009).fill(0);
for (let i = 1; i < N + 1; i++) {
  P[i] = Math.max(P[i - 1], A[i - 1]);
}
for (let i = 1; i < N + 1; i++) {
  Q[i] = Math.max(Q[i - 1], A[N - i]);
}
input.shift();
for (const i of input) {
  const [L, R] = i.split(" ").map(x => parseInt(x, 10));
  console.log(Math.max(P[L - 1], Q[N - R]));
}