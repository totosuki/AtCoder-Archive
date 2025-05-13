const [[N, K], A] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n").map(x => x.split(" ").map(y => parseInt(y, 10)));
const P = new Set();
const Q = new Set();
const M = Math.floor(N / 2);
for (let i = 1; i < (1 << M); i++) {
  let ans = 0;
  for (let j = 0; j < M; j++) {
    if (Math.floor(i / (1 << j)) % 2 == 1) {
      ans += A[j];
    }
  }
  P.add(ans);
}
for (let i = 1; i < (1 << (N - M)); i++) {
  let ans = 0;
  for (let j = 0; j < N - M; j++) {
    if (Math.floor(i / (1 << j)) % 2 == 1) {
      ans += A[M + j];
    }
  }
  Q.add(ans);
}
if (P.has(K) || Q.has(K)) {
  console.log("Yes");
} else {
  for (const i of P) {
    if (Q.has(K - i)) {
      console.log("Yes");
      process.exit();
    }
  }
  console.log("No");
}