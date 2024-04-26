const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [, X] = input[0].split(" ").map(x => parseInt(x, 10));
const P = input[1].split(" ").map(x => parseInt(x, 10));
console.log(P.indexOf(X) + 1);