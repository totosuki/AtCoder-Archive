const N = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0];
const S = ([...N].map(x => parseInt(x, 10))).reduce((a, b) => a + b);
if (parseInt(N, 10) % S === 0) {
  console.log("Yes");
} else {
  console.log("No");
}