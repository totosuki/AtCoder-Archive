const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [N, X] = (input[0].split(" ")).map(x => parseInt(x, 10));
const A = (input[1].split(" ")).map(x => parseInt(x, 10));
const L = [...(X.toString(2)).padStart(N, "0")].reverse();
let cnt = 0;
for (let i = 0; i < N; i++) {
  if (L[i] === "1") {
    cnt += A[i];
  }
}
console.log(cnt);