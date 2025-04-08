const [[, K], A] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n").map(x => x.split(" ").map(y => parseInt(y, 10)));
let L = 0, R = 1e9;
while (L < R) {
  const M = Math.floor((L + R) / 2);
  let S = 0;
  A.forEach(x => S += Math.floor(M / x));
  if (K <= S) {
    R = M;
  } else {
    L = M + 1;
  }
}
console.log(L);