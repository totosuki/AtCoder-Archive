const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [, K] = input.shift().split(" ").map(x => parseInt(x, 10));
console.log(input.slice(0, K).sort().join("\n"));