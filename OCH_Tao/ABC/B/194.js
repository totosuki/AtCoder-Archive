const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift(), 10);
let A = [];
let B = [];
let ans = Number.POSITIVE_INFINITY;
for (const i of input) {
  const [a, b] = i.split(" ").map(x => parseInt(x, 10));
  A.push(a);
  B.push(b);
}
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    ans = Math.min(ans, i === j ? A[i] + B[j] : Math.max(A[i], B[j]));
  }
}
console.log(ans);