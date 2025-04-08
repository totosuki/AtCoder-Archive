const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift(), 10);
let L = [];
for (const i of input) {
  L.push(i.split(" ").map(x => parseInt(x, 10)));
}
let ans = 0;
for (let i = 0; i < N - 1; i++) {
  for (let j = i + 1; j < N; j++) {
    ans = Math.max(ans, Math.sqrt((L[i][0] - L[j][0]) ** 2 + (L[i][1] - L[j][1]) ** 2));
  }
}
console.log(ans);