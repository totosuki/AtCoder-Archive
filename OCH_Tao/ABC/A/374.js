const S = require("fs").readFileSync("/dev/stdin", "utf8").trim();
console.log(/.*san$/.test(S) ? "Yes" : "No");