const S = require("fs").readFileSync("/dev/stdin", "utf8").trim();
console.log(/^[A-Z][1-9]\d{5}[A-Z]$/.test(S) ? "Yes" : "No");