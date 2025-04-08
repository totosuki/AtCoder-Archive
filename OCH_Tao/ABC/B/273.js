let [X, K] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
for (let i = 1; i < K + 1; i++) {
  X = Math.round(X / (10 ** i)) * (10 ** i);
}
console.log(X);