const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(str => parseInt(str, 10));
console.log((input[0] + input[1]) * input[2] / 2);