const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
console.log(S[(S.length + 1) / 2 - 1]);