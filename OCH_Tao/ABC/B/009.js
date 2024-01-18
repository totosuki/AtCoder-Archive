const A = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
const N = A.shift();
A.sort((a, b) => b - a);
const X = A[0];
let Y;
for (let i = 0; i < N; i++) {
  if (X !== A[i]) {
    Y = A[i];
    break;
  }
}
console.log(Y);