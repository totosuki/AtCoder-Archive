const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const ST = input[0].split(" ");
const S = parseInt(ST[0], 10);
const T = parseInt(ST[1], 10);
console.log(T - S + 1);