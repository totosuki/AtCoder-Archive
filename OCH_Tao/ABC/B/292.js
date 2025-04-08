const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift().split(" ")[0], 10);
let L = Array(N).fill(0);
for (const i of input) {
  const [C, X] = i.split(" ").map(x => parseInt(x, 10));
  if (C === 3) {
    console.log(L[X - 1] < 2 ? "No" : "Yes");
  } else {
    L[X - 1] += C;
  }
}