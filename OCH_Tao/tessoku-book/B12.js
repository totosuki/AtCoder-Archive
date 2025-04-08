const N = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim(), 10);
let L = 0, R = 50 * 1e6;
while (L < R) {
  const M = Math.floor((L + R) / 2);
  if (N <= (M / 1e6) ** 3 + (M / 1e6)) {
    R = M;
  } else {
    L = M + 1;
  }
}
console.log(L / 1e6);