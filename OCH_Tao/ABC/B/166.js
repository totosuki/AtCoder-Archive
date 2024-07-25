const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, K] = input.shift().split(" ").map(x => parseInt(x, 10));
let L = [];
for (let i = 0; i < K; i++) {
  input.shift();
  const A = input.shift().split(" ").map(x => parseInt(x, 10));
  L.push(...A);
}
console.log(N - [...new Set(L)].length);