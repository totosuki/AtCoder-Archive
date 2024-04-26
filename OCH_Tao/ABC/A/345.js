const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
console.log(/^<=+>$/.test(S) ? "Yes" : "No");