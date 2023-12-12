const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const MD = input[0].split(" ");
const M = parseInt(MD[0], 10);
const D = parseInt(MD[1], 10);
if (M % D === 0) {
  console.log("YES");
} else {
  console.log("NO");
}