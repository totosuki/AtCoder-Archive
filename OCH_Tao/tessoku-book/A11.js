const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, X] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ").map(x => parseInt(x, 10));
let L = 0;
let R = N - 1;
while (L <= R) {
  let M = Math.floor((L + R) / 2);
  if (X === A[M]) {
    console.log(M + 1);
    break;
  }
  if (X < A[M]) {
    R = M - 1;
  }
  if (X > A[M]) {
    L = M + 1;
  }
}