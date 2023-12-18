const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const S = [...input[0]];
const N = parseInt(input[1], 10);
let x = Math.trunc((N - 1) / 5);
let y = (N - 1) % 5;
console.log(S[x] + S[y]);