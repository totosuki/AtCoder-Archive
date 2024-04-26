const W = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(W.shift(), 10);
if (W.length !== [...new Set(W)].length) {
  console.log("No");
} else {
  for (let i = 1; i < N; i++) {
    if (W[i - 1][W[i - 1].length - 1] !== W[i][0]) {
      console.log("No");
      break;
    }
    if (i === N - 1) {
      console.log("Yes");
    }
  }
}