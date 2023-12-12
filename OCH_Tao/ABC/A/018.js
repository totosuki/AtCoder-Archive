const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = input.map(str => parseInt(str, 10));
const sortedN = [...N];
sortedN.sort((a, b) => b - a);
for (let i = 0; i < 3; i++) {
  console.log((sortedN.indexOf(N[i])) + 1);
}