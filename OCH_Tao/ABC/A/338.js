const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
console.log(/^[A-Z][a-z]*$/.test(S) ? "Yes" : "No");