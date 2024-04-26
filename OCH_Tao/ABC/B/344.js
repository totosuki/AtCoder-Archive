const A = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
A.reverse();
console.log(A.join("\n"));