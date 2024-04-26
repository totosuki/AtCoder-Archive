const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
console.log(S.replaceAll("a", "").replaceAll("e", "").replaceAll("i", "").replaceAll("o", "").replaceAll("u", ""));