const S = require("fs").readFileSync("/dev/stdin", "utf8").trim();
console.log(/[A-Z]/.test(S) && /[a-z]/.test(S) && S.length === new Set([...S]).size ? "Yes" : "No");