const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
const B = input[2].split(" ").map(x => parseInt(x, 10));
const C = input[3].split(" ").map(x => parseInt(x, 10));
let cnt = 0;
for (let i = 0; i < N; i++) {
  cnt += B[A[i] - 1];
  if (i > 0) {
    if (A[i] - A[i - 1] === 1) {
      cnt += C[A[i - 1] - 1];
    }
  }
}
console.log(cnt);