const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
let L = [];
for (let i = 0; i < S.length - 2; i++) {
  L.push(parseInt(S.slice(i, i + 3), 10));
}
let diff = L.map(X => Math.abs(753 - X));
console.log(Math.min(...diff));