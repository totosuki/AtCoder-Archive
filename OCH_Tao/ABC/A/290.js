const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const A = input[1].split(" ").map(x => parseInt(x, 10));
const B = input[2].split(" ").map(x => parseInt(x, 10));
let cnt = 0;
for (const i of B) {
  cnt += A[i - 1];
}
console.log(cnt);