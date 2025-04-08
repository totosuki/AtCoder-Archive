const [, A, B] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n").map(x => x.split(" ").map(y => parseInt(y, 10)));
console.log(Math.max(...A) + Math.max(...B));