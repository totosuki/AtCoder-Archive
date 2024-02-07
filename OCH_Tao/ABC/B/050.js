const X = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(X.shift(), 10);
const T = (X.shift().split(" ")).map(x => parseInt(x, 10));
const M = parseInt(X.shift(), 10);
const SUM = T.reduce((a, b) => a + b);
for (let i = 0; i < M; i++) {
  let [p, x] = (X[i].split(" ")).map(x => parseInt(x, 10));
  console.log(SUM - T[p - 1] + x);
}