const X = require("fs").readFileSync("/dev/stdin", "utf8").trim();
const S = "1234567890123";
console.log([...new Set([...X])].length === 1 || S.includes(X) ? "Weak" : "Strong");