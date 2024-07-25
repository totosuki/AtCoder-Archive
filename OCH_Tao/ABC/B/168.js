const [K, S] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
console.log(S.length <= parseInt(K, 10) ? S : S.slice(0, parseInt(K, 10)) + "...");