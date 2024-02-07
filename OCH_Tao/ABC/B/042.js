const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [N, L] = (S.shift()).split(" ");
S.sort();
console.log(S.join(""));