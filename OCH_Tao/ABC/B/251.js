const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, W] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ").map(x => parseInt(x, 10));
let S = new Set();
A.forEach(x => S.add(x));
for (let i = 0; i < N - 1; i++) {
  for (let j = i + 1; j < N; j++) {
    S.add(A[i] + A[j]);
  }
}
for (let i = 0; i < N - 2; i++) {
  for (let j = i + 1; j < N - 1; j++) {
    for (let k = j + 1; k < N; k++) {
      S.add(A[i] + A[j] + A[k]);
    }
  }
}
console.log([...S].filter(x => x <= W).length);