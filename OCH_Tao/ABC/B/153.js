const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const H = parseInt(input[0].split(" ")[0], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
console.log(H <= A.reduce((a, b) => a + b, 0) ? "Yes" : "No");