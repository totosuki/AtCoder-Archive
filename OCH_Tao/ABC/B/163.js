const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0].split(" ")[0], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
console.log(Math.max(N - A.reduce((a, b) => a + b, 0), -1));