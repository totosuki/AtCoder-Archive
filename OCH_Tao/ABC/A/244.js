const [N, S] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
console.log(S.charAt(parseInt(N, 10) - 1));