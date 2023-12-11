const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const N = parseInt(input[0], 10);
if (input[0].includes("3")) {
  console.log("YES");
} else if (N % 3 === 0) {
  console.log("YES");
} else {
  console.log("NO");
}