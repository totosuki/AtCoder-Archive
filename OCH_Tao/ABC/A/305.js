const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
let P = [];
for (let i = 0; i < 101; i += 5) {
  P.push(i);
}
const X = P.map(x => Math.abs(N - x));
console.log(P[X.indexOf(Math.min(...X))]);