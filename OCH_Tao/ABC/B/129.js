const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const W = (input[1].split(" ")).map(x => parseInt(x, 10));
let cnt = [];
for (let i = 1; i < N; i++) {
  const X = [...W.slice(0, i)].reduce((a, b) => a + b, 0);
  const Y = [...W.slice(i)].reduce((a, b) => a + b, 0);
  cnt.push(Math.abs(X - Y));
}
console.log(Math.min(...cnt));