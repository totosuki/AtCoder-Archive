const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift(), 10);
let M = new Map();
for (const i of input) {
  const [A, B] = i.split(" ").map(x => parseInt(x, 10));
  M.set(A, (M.get(A) ?? 0) + 1);
  M.set(B, (M.get(B) ?? 0) + 1);
}
console.log(Math.max(...M.values()) === N - 1 && M.size === N ? "Yes" : "No");