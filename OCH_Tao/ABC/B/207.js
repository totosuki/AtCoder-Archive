const [A, B, C, D] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
console.log(0 < C * D - B ? Math.ceil(A / (C * D - B)) : -1);