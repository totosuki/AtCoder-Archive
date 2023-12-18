const input = require("fs").readFileSync("/dev/stdin", "utf8").trim();
const L = [...input].map(str => parseInt(str, 10));
console.log(L[0] + L[1]);