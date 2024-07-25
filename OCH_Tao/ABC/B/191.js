const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const X = parseInt(input[0].split(" ")[1], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
console.log(A.filter(x => x !== X).join(" "));