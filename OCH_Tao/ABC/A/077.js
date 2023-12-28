const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const X = input[0];
const Y = input[1];
if (X[0] === Y[2] && X[1] === Y[1] && X[2] === Y[0]) {
  console.log("YES")
} else {
  console.log("NO")
}