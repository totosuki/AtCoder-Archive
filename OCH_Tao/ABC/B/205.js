const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
let A = input[1].split(" ").map(x => parseInt(x, 10));
A.sort((a, b) => a - b);
for (let i = 0; i < N; i++) {
  if (A[i] !== i + 1) {
    console.log("No");
    return 0;
  }
}
console.log("Yes");