const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
let l = [];
for (let i = 1; i < N + 1; i++) {
  l.push(Math.abs(Math.trunc(N / i) - i) + N % i);
}
if (N === 1) {
  console.log(0);
} else {
  console.log(Math.min(...l));
}