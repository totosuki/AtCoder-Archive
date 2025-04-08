const S = require("fs").readFileSync("/dev/stdin", "utf8").trim();
console.log("oxx".repeat(1e5).includes(S) ? "Yes" : "No");