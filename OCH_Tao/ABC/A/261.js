const [L1, R1, L2, R2] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0].split(" ").map(x => parseInt(x, 10));
console.log(Math.max(0, Math.min(R1, R2) - Math.max(L1, L2)));