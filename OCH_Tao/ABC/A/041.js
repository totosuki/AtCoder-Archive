const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const S = input[0];
const I = parseInt(input[1], 10);
console.log(S[I - 1]);