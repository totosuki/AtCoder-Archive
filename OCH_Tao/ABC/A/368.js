const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, K] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ").map(x => parseInt(x, 10));
console.log(A.slice(N - K).concat(A.slice(0, N - K)).join(" "));