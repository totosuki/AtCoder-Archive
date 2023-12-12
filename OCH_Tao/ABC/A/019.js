const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const L = input[0].split(" ");
const abcL = L.map(str => parseInt(str, 10));
abcL.sort((a, b) => a - b);
console.log(abcL[1]);