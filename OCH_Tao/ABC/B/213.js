const A = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ");
console.log(A.indexOf([...A].sort((a, b) => b - a)[1]) + 1);