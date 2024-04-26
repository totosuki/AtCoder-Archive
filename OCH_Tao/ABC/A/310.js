const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [, P, Q] = input[0].split(" ").map(x => parseInt(x, 10));
const D = input[1].split(" ").map(x => parseInt(x, 10));
console.log(Math.min(P, Q + Math.min(...D)));