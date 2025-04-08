const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
let L = [];
for (let i = 0; i < N - 1; i++) {
  if (A[i] < A[i + 1]) {
    for (let j = A[i]; j < A[i + 1]; j++) {
      L.push(j);
    }
  } else {
    for (let j = A[i]; j > A[i + 1]; j--) {
      L.push(j);
    }
  }
}
L.push(A[N - 1]);
console.log(...L);