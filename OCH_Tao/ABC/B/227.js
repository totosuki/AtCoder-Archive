const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(x => parseInt(x, 10));
let X = new Set();
for (let a = 1; a < 1001; a++) {
  for (let b = 1; b < 1001; b++) {
    X.add(4 * a * b + 3 * a + 3 * b);
  }
}
console.log(S.filter(x => !X.has(x)).length);