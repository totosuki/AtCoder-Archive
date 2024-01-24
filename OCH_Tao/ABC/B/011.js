const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
console.log((S[0]).toUpperCase() + (S.slice(1)).toLowerCase());