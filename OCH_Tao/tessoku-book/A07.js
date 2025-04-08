const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const D = parseInt(input.shift(), 10);
input.shift();
let X = Array(D + 1).fill(0);
for (const i of input) {
  const [L, R] = i.split(" ").map(x => parseInt(x, 10));
  X[L - 1]++;
  X[R]--;
}
let ans = [0];
for (let i = 0; i < D; i++) {
  ans.push(ans[i] + X[i]);
}
for (const i of ans.slice(1)) {
  console.log(i);
}