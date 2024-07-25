const [N, K] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
let cnt = 0;
for (let i = 1; i < N + 1; i++) {
  for (let j = 1; j < K + 1; j++) {
    cnt += 100 * i + j;
  }
}
console.log(cnt);