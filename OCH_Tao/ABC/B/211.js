const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
console.log([...new Set(S)].length === 4 ? "Yes" : "No");