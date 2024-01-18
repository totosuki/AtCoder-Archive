const W = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
console.log(W.replaceAll("a", "").replaceAll("i", "").replaceAll("u", "").replaceAll("e", "").replaceAll("o", ""));