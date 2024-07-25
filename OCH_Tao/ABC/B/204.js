const A = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(x => parseInt(x, 10));
console.log(A.map(x => x > 10 ? x - 10 : 0).reduce((a, b) => a + b, 0));