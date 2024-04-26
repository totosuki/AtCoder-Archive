const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const V = (input[1].split(" ")).map(x => parseInt(x, 10));
const C = (input[2].split(" ")).map(x => parseInt(x, 10));
let diff = [];
for (let i = 0; i < N; i++) {
  const X = V[i] - C[i];
  if (X > 0) {
    diff.push(X);
  }
}
console.log(diff.reduce((a, b) => a + b, 0));