const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift().split(" ")[0], 10);
const A = new Set(input.shift().split(" ").map(x => parseInt(x, 10)));
let L = [];
let R = [];
for (let i = 0; i < N; i++) {
  if (A.has(i + 1)) {
    R.push(input[i].split(" ").map(x => parseInt(x, 10)));
  } else {
    L.push(input[i].split(" ").map(x => parseInt(x, 10)));
  }
}
let ans = new Array(L.length).fill(Infinity);
for (const i of R) {
  for (let j = 0; j < L.length; j++) {
    ans[j] = Math.min(ans[j], ((i[0] - L[j][0]) ** 2 + (i[1] - L[j][1]) ** 2) ** (1 / 2));
  }
}
console.log(Math.max(...ans));