const [S, T] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
console.log(S === T.slice(0, S.length) ? "Yes" : "No");