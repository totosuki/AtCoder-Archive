const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
let L = [];
for (let i = 0; i < N; i++) {
  const X = A.slice(7 * i, 7 * (i + 1));
  L.push(X.reduce((a, b) => a + b, 0));
}
console.log(L.join(" "));