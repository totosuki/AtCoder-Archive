const X = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(x => parseInt(x, 10));
console.log(X.map(Math.abs).reduce((a, b) => a + b));
console.log(Math.sqrt(X.map(x => Math.abs(x) ** 2).reduce((a, b) => a + b)));
console.log(Math.max(...X.map(Math.abs)));