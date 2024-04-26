const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[1];
console.log(S.includes("ab") || S.includes("ba") ? "Yes" : "No");