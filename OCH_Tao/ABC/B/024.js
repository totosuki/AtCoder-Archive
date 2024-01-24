const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [N, T] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
const A = [...input].map(x => parseInt(x, 10));
let time = null;
let cnt = 0;
for (let i = 0; i < N; i++) {
  if (!time) {
    time = A[i] + T;
  } else {
    if (A[i] > time) {
      cnt += T;
      time = A[i] + T;
    } else {
      cnt += T - (time - A[i]);
      time = A[i] + T;
    }
  }
}
cnt += T;
console.log(cnt);