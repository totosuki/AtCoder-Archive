const A = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ");
console.log(new Set(A).size);