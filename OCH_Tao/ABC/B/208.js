let P = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim(), 10);
const X = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1];
let cnt = 0;
for (const i of X) {
  cnt += Math.floor(P / i);
  P %= i;
}
console.log(cnt);