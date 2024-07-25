const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [, K, X] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ").map(x => parseInt(x, 10));
A.splice(K, 0, X);
console.log(A.join` `);