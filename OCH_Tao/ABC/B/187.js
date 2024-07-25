const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift(), 10);
let L = [];
let ans = [];
for (const i of input) {
  L.push(i.split(" ").map(x => parseInt(x, 10)));
}
for (let i = 0; i < N - 1; i++) {
  for (let j = i + 1; j < N; j++) {
    ans.push((L[i][1] - L[j][1]) / (L[i][0] - L[j][0]));
  }
}
console.log(ans.filter(x => -1 <= x && x <= 1).length);