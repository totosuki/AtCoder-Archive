const A = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[1].split(" ").map(x => parseInt(x, 10));
console.log(0 - A.reduce((a, b) => a + b, 0));