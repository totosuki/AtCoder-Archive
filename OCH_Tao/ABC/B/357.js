const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0];
console.log((S.match(/[A-Z]/g) ?? []).length > (S.match(/[a-z]/g) ?? []).length ? S.toUpperCase() : S.toLowerCase());