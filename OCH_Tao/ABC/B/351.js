const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input.shift(), 10);
let A = [];
let B = [];
for (let i = 0; i < N; i++) {
  A.push([...input.shift()]);
}
for (let i = 0; i < N; i++) {
  B.push([...input.shift()]);
}
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (A[i][j] !== B[i][j]) {
      console.log(`${i + 1} ${j + 1}`);
      break;
    }
  }
}