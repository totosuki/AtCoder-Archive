const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, X] = input.shift().split(" ").map(x => parseInt(x, 10));
let cnt = 0;
for (let i = 0; i < N; i++) {
  const [V, P] = input[i].split(" ").map(x => parseInt(x, 10));
  cnt += V * P;
  if (cnt > X * 100) {
    console.log(i + 1);
    return false;
  }
}
console.log(-1);