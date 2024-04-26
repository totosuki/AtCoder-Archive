const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
const A = (input[1].split(" ")).map(x => parseInt(x, 10));
A.sort((a, b) => b - a);
let cnt = 0;
for (let i = 0; i < N; i++) {
  if (i % 2 === 0) {
    cnt += A[i];
  } else {
    cnt -= A[i];
  }
}
console.log(cnt);