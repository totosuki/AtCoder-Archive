let [A, B, C, K] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0].split(" ").map(x => parseInt(x, 10));
let cnt = 0;
cnt += Math.min(A, K);
K = Math.max(0, K - A);
K = Math.max(0, K - B);
cnt -= Math.min(C, K);
K = Math.max(0, K - C);
console.log(cnt);