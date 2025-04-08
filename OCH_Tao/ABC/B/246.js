const [A, B] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
const D = Math.atan2(B, A);
console.log(Math.cos(D), Math.sin(D));