const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
let S = new Set([...Array(N).keys()].map(x => x + 1));
for (let i = 0; i < N; i++) {
  if (S.has(i + 1)) {
    S.delete(A[i]);
  }
}
console.log(S.size);
console.log([...S].sort((a, b) => a - b).join(" "));