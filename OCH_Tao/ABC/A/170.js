const X = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
console.log(X.indexOf("0") + 1);