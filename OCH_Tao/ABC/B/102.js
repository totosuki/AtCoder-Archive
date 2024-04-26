const A = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ")).map(x => parseInt(x, 10));
console.log(Math.max(...A) - Math.min(...A));