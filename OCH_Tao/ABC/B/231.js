const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
input.shift();
let M = new Map();
for (const i of input) {
  M.set(i, (M.get(i) ?? 0) + 1);
}
console.log([...M].sort((a, b) => b[1] - a[1])[0][0]);