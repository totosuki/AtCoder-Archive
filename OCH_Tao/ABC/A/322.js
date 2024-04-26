const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[1];
const X = S.indexOf("ABC");
console.log(X >= 0 ? X + 1 : X);