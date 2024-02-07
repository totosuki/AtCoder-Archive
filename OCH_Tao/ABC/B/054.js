const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [N, M] = (input.shift().split(" ")).map(x => parseInt(x, 10));
let A = [];
let B = [];
for (let i = 0; i < N; i++) {
  A.push(input.shift());
}
for (let i = 0; i < M; i++) {
  B.push(input.shift());
}
for (let i = 0; i < N - M + 1; i++) {
  if (A[i].includes(B[0])) {
    let x = A[i].indexOf(B[0]);
    for (let j = 1; j < M; j++) {
      if (A[i + j].slice(x, x + M) !== B[j]) {
        break;
      }
    }
    console.log("Yes");
    break;
  }
  console.log("No");
  break;
}