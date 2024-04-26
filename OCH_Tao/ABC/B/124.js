const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const H = (input[1].split(" ")).map(x => parseInt(x, 10));
let cnt = 1;
for (let i = 1; i < N; i++) {
  const X = H.slice(0, i);
  if (X.every(x => x <= H[i])) {
    cnt++;
  }
}
console.log(cnt);