const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1];
console.log(S.indexOf("1") % 2 === 0 ? "Takahashi" : "Aoki");