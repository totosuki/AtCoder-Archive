const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
let l = (input[0].split(" ")).map(x => parseInt(x, 10));
const K = parseInt(input[1], 10);
l.sort((a, b) => b - a);
for (let i = 0; i < K; i++) {
  l[0] *= 2;
}
console.log(l.reduce((a, b) => a + b));