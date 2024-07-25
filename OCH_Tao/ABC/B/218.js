const P = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
console.log(P.map(x => String.fromCharCode(96 + x)).join(""));