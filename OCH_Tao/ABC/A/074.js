const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
console.log(input[0] ** 2 - input[1]);