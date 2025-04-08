const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, T] = input[0].split(" ").map(x => parseInt(x, 10));
const C = input[1].split(" ").map(x => parseInt(x, 10));
const R = input[2].split(" ").map(x => parseInt(x, 10));
const X = C.includes(T) ? T : C[0];
let L = [];
for (let i = 0; i < N; i++) {
  if (C[i] === X) {
    L.push([R[i], i + 1]);
  }
}
L.sort((a, b) => b[0] - a[0]);
console.log(L[0][1]);