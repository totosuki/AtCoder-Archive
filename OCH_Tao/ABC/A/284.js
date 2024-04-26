const [, ...S] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
S.reverse();
console.log(S.join("\n"));