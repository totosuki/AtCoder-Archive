const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt((input.shift()), 10);
let S = [];
let P = [];
for (let i = 0; i < N; i++) {
  let [x, y] = input[i].split(" ");
  S.push(x);
  P.push(parseInt(y, 10));
}
const T = P.reduce((a, b) => a + b);
const X = P.findIndex((x) => x > T / 2);
if (X === -1) {
  console.log("atcoder");
} else {
  console.log(S[X]);
}