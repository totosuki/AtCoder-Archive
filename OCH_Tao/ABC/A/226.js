const X = parseFloat((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]);
console.log(Math.round(X));