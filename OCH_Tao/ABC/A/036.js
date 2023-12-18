const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(str => parseInt(str, 10));
console.log(Math.ceil(input[1] / input[0]));