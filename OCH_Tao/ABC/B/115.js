const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift(), 10);
const P = input.map(x => parseInt(x, 10));
console.log(P.reduce((a, b) => a + b) - Math.max(...P) / 2);