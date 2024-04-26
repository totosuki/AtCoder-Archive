const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const P = (input[1].split(" ")).map(x => parseInt(x, 10));
let cnt = 0;
for (let i = 1; i < N - 1; i++) {
  if ((P[i - 1] < P[i] && P[i] < P[i + 1]) || (P[i - 1] > P[i] && P[i] > P[i + 1])) {
    cnt++;
  }
}
console.log(cnt);