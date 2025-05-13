const [[N, K], A] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n").map(x => x.split(" ").map(y => parseInt(y, 10)));
let B = [0];
for (let i = 0; i < N; i++) {
  B.push(B[B.length - 1] + A[i]);
}
let ans = 0;
let R = 1;
for (let i = 1; i < N + 1; i++) {
  while (R <= N && B[R] - B[i - 1] <= K) {
    R++;
  }
  ans += R - i;
}
console.log(ans);