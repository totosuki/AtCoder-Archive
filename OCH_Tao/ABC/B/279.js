const [S, T] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
console.log(S.includes(T) ? "Yes" : "No");