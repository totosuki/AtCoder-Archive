const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [, A, B] = input[0].split(" ").map(x => parseInt(x, 10));
const C = input[1].split(" ").map(x => parseInt(x, 10));
console.log(C.indexOf(A + B) + 1);