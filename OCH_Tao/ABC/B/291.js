const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const X = input[1].split(" ").map(x => parseInt(x, 10));
X.sort((a, b) => a - b);
console.log(X.slice(N, 4 * N).reduce((a, b) => a + b, 0) / (3 * N));