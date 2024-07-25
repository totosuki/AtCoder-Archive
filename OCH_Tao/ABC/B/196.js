const X = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0];
console.log(X.includes(".") ? X.slice(0, X.indexOf(".")) : X);