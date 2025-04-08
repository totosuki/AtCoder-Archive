const [P, Q] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 36) - 10);
const L = [0, 3, 4, 8, 9, 14, 23];
console.log(Math.abs(L[P] - L[Q]));