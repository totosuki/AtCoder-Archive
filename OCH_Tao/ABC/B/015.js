const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
const A = (input[1].split(" ")).map(x => parseInt(x, 10));
let bug = A.filter((x) => x != 0);
console.log(Math.ceil(bug.reduce((a, b) => a + b, 0) / bug.length));