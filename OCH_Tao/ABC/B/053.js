const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
let l = S.match(/A[A-Z]*Z/g);
console.log(Math.max([...l.map(x => x.length)]));