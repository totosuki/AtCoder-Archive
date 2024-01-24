const A = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
const N = A.shift();
let l = [...new Set(A)];
console.log(A.length - l.length);