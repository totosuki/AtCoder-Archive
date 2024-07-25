const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0].length;
console.log("x".repeat(S));