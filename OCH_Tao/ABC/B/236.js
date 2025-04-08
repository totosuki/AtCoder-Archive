const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
console.log(N * (N + 1) * 2 - A.reduce((a, b) => a + b, 0));