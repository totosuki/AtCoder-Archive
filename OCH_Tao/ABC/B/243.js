const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const A = input[1].split(" ");
const B = input[2].split(" ");
let cnt = 0;
let X = new Set();
let Y = new Set();
for (let i = 0; i < N; i++) {
  if (A[i] === B[i]) {
    cnt++;
  } else {
    X.add(A[i]);
    Y.add(B[i]);
  }
}
console.log(cnt);
let ans = new Set();
for (const i of X) {
  if (Y.has(i)) {
    ans.add(i);
  }
}
console.log(ans.size);