const X = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
X.splice(0, 1);
console.log(Math.min(...X));