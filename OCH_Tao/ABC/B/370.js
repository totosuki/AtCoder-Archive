const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
let A = [];
for (let i = 1; i < N + 1; i++) {
  A.push(input[i].split(" ").map(x => parseInt(x, 10)));
}
let ans = 1;
for (let i = 0; i < N; i++) {
  let tmp = [ans - 1, i];
  ans = A[Math.max(...tmp)][Math.min(...tmp)];
}
console.log(ans);