const [L, R] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => Boolean(parseInt(x, 2)));
console.log(L && !R ? "Yes" : !L && R ? "No" : "Invalid");