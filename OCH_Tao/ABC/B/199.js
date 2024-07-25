const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const A = input[1].split(" ").map(x => parseInt(x, 10));
const B = input[2].split(" ").map(x => parseInt(x, 10));
console.log(Math.max(0, Math.min(...B) - Math.max(...A) + 1));