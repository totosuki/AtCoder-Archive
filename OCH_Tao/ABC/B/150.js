const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1];
console.log((S.match(/ABC/g) ?? []).length);