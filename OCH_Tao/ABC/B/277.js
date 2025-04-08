const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(S.shift(), 10);
const RE = new RegExp("^[HDCS][A23456789TJQK]$");
console.log(new Set(S.filter(x => RE.test(x))).size === N ? "Yes" : "No");