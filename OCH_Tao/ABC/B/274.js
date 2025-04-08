const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [, W] = input.shift().split(" ").map(x => parseInt(x, 10));
let X = new Array(W).fill(0);
for (const C of input) {
  for (let i = 0; i < W; i++) {
    if (C[i] === "#") {
      X[i]++;
    }
  }
}
console.log(X.join(" "));