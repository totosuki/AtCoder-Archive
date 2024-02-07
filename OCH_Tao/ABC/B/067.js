const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [N, K] = (input[0].split(" ")).map(x => parseInt(x, 10));
let l = (input[1].split(" ")).map(x => parseInt(x, 10));
l.sort((a, b) => b - a);
const S = l.slice(0, K);
console.log(S.reduce((a, b) => a + b));