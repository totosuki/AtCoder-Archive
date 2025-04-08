const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
let L = [0];
for (let i = 0; i < N; i++) {
  L.push((L[L.length - 1] + A[i]) % 360);
}
L.push(360);
L.sort((a, b) => b - a);
let cnt = [];
for (let i = 0; i < N + 1; i++) {
  cnt.push(L[i] - L[i + 1]);
}
console.log(Math.max(...cnt));