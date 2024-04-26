const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(".");
console.log(S[S.length - 1]);