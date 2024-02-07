const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
console.log(S[0] + String(S.length - 2) + S[S.length - 1]);