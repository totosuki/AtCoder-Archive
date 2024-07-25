const X = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0];
console.log(X === "AtCoder Land" ? "Yes" : "No");