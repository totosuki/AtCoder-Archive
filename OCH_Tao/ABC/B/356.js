const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const M = parseInt(input.shift().split(" ")[1], 10);
let A = input.shift().split(" ").map(x => parseInt(x, 10));
for (const i of input) {
  const X = i.split(" ").map(x => parseInt(x, 10));
  for (let i = 0; i < M; i++) {
    A[i] -= X[i];
  }
}
console.log(A.every(x => x <= 0) ? "Yes" : "No");