const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
const K = parseInt(input[1], 10);
const X = (input[2].split(" ")).map(x => parseInt(x, 10));
let l = [];
for (let i = 0; i < N; i++) {
  l.push(2 * (Math.min(X[i], K - X[i])));
}
console.log(l.reduce((a, b) => a + b));