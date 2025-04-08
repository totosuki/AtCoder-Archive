const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const T = parseInt(input.shift(), 10);
input.shift();
let X = Array(T + 1).fill(0);
for (const i of input) {
  const [L, R] = i.split(" ").map(x => parseInt(x, 10));
  X[L]++;
  X[R]--;
}
let ans = [0];
for (let i = 0; i < T; i++) {
  ans.push(ans[i] + X[i]);
}
for (let i = 1; i < T + 1; i++) {
  console.log(ans[i]);
}