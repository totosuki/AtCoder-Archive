const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [, S, D] = input.shift().split(" ").map(x => parseInt(x, 10));
for (const i of input) {
  const [X, Y] = i.split(" ").map(x => parseInt(x, 10));
  if (X < S && Y > D) {
    console.log("Yes");
    return false;
  }
}
console.log("No");