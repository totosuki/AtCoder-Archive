const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, M] = input.shift().split(" ").map(x => parseInt(x, 10));
let X = new Array(N).fill().map(() => new Set());
for (let i = 0; i < M; i++) {
  let [, ...x] = input[i].split(" ").map(x => parseInt(x, 10));
  for (const j of x) {
    for (const k of x) {
      X[j - 1].add(k);
    }
  }
}
console.log(X.every(x => x.size === N) ? "Yes" : "No");