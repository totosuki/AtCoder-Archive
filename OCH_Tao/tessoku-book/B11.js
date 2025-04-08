const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
A.sort((a, b) => a - b);
const Q = parseInt(input[2], 10);
for (let i = 3; i < Q + 3; i++) {
  const X = parseInt(input[i], 10);
  let L = 0;
  let R = N;
  while (L < R) {
    const M = Math.floor((L + R) / 2);
    if (A[M] < X) {
      L = M + 1;
    } else {
      R = M;
    }
  }
  console.log(L);
}