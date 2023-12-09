const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const num = input[0].split(" ");
const X = parseInt(num[0], 10);
const Y = parseInt(num[1], 10);
if (X > Y) {
  console.log(X);
} else {
  console.log(Y);
}