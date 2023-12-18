const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const A = parseInt(input[0], 10);
console.log((A / 2) ** 2);