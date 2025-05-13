const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, K] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ").map(x => parseInt(x, 10));
let R = Array(100009).fill(0);
let ans = 0;
for (let i = 1; i < N; i++) {
  if (i == 1) {
    R[i] = 1;
  } else {
    R[i] = R[i - 1];
  }
  while (R[i] < N && A[R[i]] - A[i - 1] <= K) {
    R[i]++;
  }
  ans += R[i] - i;
}
console.log(ans);