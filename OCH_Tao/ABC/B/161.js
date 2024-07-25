const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, M] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ").map(x => parseInt(x, 10));
console.log(A.filter(x => x >= A.reduce((a, b) => a + b, 0) / (4 * M)).length >= M ? "Yes" : "No");