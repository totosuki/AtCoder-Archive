const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, Q] = input.shift().split(" ").map(x => parseInt(x, 10));
let L = [];
for (let i = 0; i < N; i++) {
  const X = input[i].split(" ");
  L.push(X);
}
for (let i = N; i < N + Q; i++) {
  const [S, T] = input[i].split(" ").map(x => parseInt(x, 10));
  console.log(L[S - 1][T]);
}