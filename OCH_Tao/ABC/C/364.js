const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, X, Y] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ").map(x => parseInt(x, 10));
const B = input[2].split(" ").map(x => parseInt(x, 10));
A.sort((a, b) => b - a);
B.sort((a, b) => b - a);
let cntA = 0;
let cntB = 0;
for (let i = 0; i < N; i++) {
  cntA += A[i];
  cntB += B[i];
  if (cntA > X || cntB > Y) {
    console.log(i + 1);
    process.exit();
  }
}
console.log(N);