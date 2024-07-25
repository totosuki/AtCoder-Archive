const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
let cnt = 0;
for (let i = 1; i < N + 1; i++) {
  if (Math.abs(A.indexOf(i) - A.lastIndexOf(i)) === 2) {
    cnt++;
  }
}
console.log(cnt);