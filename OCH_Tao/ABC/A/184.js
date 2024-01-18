const [ab, cd] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [A, B] = (ab.split(" ")).map(x => parseInt(x, 10));
const [C, D] = (cd.split(" ")).map(x => parseInt(x, 10));
console.log(A * D - B * C);