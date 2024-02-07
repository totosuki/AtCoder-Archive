const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].repeat(6);
console.log(S.slice(0, 6));