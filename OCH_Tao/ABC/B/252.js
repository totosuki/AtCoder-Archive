const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const A = input[1].split(" ").map(x => parseInt(x, 10));
const B = input[2].split(" ").map(x => parseInt(x, 10));
let X = new Set();
for (const [i, j] of A.entries()) {
  if (j === Math.max(...A)) {
    X.add(i + 1);
  }
}
for (const i of B) {
  if (X.has(i)) {
    console.log("Yes");
    return false;
  }
}
console.log("No");