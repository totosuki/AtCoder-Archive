const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, K,] = input[0].split(" ").map(x => parseInt(x, 10));
let A = input[1].split(" ").map(x => parseInt(x, 10));
const L = input[2].split(" ").map(x => parseInt(x, 10));
for (const i of L) {
  if (A[i - 1] === N) {
    continue;
  } else if (i === K) {
    A[i - 1]++;
  } else if (A[i - 1] < A[i] - 1) {
    A[i - 1]++;
  }
}
console.log(...A);