const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const K = parseInt(input[0], 10);
const [A, B] = input[1].split(" ").map(x => parseInt(x, K));
console.log(A * B);