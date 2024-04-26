const A = "atcoder";
const [L, R] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ").map(x => parseInt(x, 10));
console.log(A.slice(L - 1, R));