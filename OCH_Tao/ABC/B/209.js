const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, X] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ").map(x => parseInt(x, 10));
console.log(A.reduce((a, b) => a + b, 0) - Math.floor(N / 2) <= X ? "Yes" : "No");