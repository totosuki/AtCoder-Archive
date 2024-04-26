const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
let [N, X] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
const M = input.map(x => parseInt(x, 10));
M.sort((a, b) => a - b);
let cnt = N;
X -= M.reduce((a, b) => a + b);
while (X >= M[0]) {
  X -= M[0];
  cnt++;
}
console.log(cnt);