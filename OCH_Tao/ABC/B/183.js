const [SX, SY, GX, GY] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0].split(" ").map(x => parseInt(x, 10));
console.log(SX + (SY / (SY + GY)) * (GX - SX));