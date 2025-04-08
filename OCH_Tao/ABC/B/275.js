const [A, B, C, D, E, F] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(BigInt);
console.log(((A * B * C - D * E * F) % 998244353n).toString());