const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
const X = [...S.match(/[ACGT]*/g)].map(x => x.length);
console.log(Math.max(...X));