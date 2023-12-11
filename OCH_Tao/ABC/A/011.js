const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const N = parseInt(input[0], 10);
if (N === 12) {
  console.log(1);
} else {
  console.log(N + 1);
}