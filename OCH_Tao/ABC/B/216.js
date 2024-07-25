const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift(), 10);
console.log([...new Set(input)].length !== N ? "Yes" : "No");