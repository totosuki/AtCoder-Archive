const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, K] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ").map(x => parseInt(x, 10));
A.sort((a, b) => a - b);
let ans = 1e10;
for (let i = 0; i < K + 1; i++) {
  ans = Math.min(ans, A[i + (N - K) - 1] - A[i]);
}
console.log(ans);