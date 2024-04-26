const D = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = D.shift();
console.log([...new Set(D)].length);