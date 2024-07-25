const X = require("fs").readFileSync("/dev/stdin", "utf8").trim();
console.log((X.match(/T/g) ?? []).length);