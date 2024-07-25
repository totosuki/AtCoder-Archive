const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
let X = parseInt(input[0].split(" ")[1], 10);
const S = [...input[1]];
for (const i of S) {
  if (i == "o") {
    X++;
  } else {
    X = Math.max(0, X - 1);
  }
}
console.log(X);