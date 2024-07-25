const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, K, M] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ").map(x => parseInt(x, 10));
const SUM = A.reduce((a, b) => a + b, 0);
console.log(N * M - SUM <= K ? Math.max(0, N * M - SUM) : -1);