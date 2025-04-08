const S = require("fs").readFileSync("/dev/stdin", "utf8").trim();
console.log(S.replaceAll(".", ""));