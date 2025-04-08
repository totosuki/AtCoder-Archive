const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n").map(x => [...x]);
let A = 1e8;
let B = -1e8;
let C = 1e8;
let D = -1e8;
for (let i = 0; i < 10; i++) {
  for (let j = 0; j < 10; j++) {
    if (S[i][j] === "#") {
      A = Math.min(A, i + 1);
      B = Math.max(B, i + 1);
      C = Math.min(C, j + 1);
      D = Math.max(D, j + 1);
    }
  }
}
console.log(A, B);
console.log(C, D);