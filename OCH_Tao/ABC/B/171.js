const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const K = parseInt(input[0].split(" ")[1], 10);
let P = input[1].split(" ").map(x => parseInt(x, 10));
P.sort((a, b) => a - b);
console.log(P.slice(0, K).reduce((a, b) => a + b, 0));