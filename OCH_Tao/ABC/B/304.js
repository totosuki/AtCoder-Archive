const N = require("fs").readFileSync("/dev/stdin", "utf8").trim();
console.log(N.length < 4 ? N : N.slice(0, 3) + "0".repeat(N.length - 3));