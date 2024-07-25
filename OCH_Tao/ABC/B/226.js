const A = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
console.log([...new Set(A)].length - 1);