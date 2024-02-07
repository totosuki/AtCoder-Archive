const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
const A = (input[1].split(" ")).map(x => parseInt(x, 10));
A.sort((a, b) => b - a);
console.log(A[0] - A[A.length - 1]);