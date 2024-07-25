const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [, T, P] = input[0].split(" ").map(x => parseInt(x, 10));
const L = input[1].split(" ").map(x => parseInt(x, 10));
L.sort((a, b) => b - a);
console.log(Math.max(0, T - L[P - 1]));