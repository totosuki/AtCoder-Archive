const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const T = S.pop();
console.log(T.replaceAll("1", S[0]).replaceAll("2", S[1]).replaceAll("3", S[2]));