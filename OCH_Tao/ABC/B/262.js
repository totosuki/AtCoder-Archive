const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N,] = input.shift().split(" ").map(x => parseInt(x, 10));
let cnt = new Array(N).fill(0).map(x => x = new Array(N).fill(false));
for (const i of input) {
  const [U, V] = i.split(" ").map(x => parseInt(x, 10));
  cnt[U - 1][V - 1] = true;
  cnt[V - 1][U - 1] = true;
}
let ans = 0;
for (let i = 0; i < N - 2; i++) {
  for (let j = i; j < N - 1; j++) {
    for (let k = j; k < N; k++) {
      if (cnt[i][j] && cnt[j][k] && cnt[k][i]) {
        ans++;
      }
    }
  }
}
console.log(ans);