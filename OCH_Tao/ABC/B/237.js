const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [, W] = input.shift().split(" ").map(x => parseInt(x, 10));
let A = [];
for (const i of input) {
  A.push(i.split(" "));
}
for (let i = 0; i < W; i++) {
  console.log(A.map(x => x[i]).join(" "));
}