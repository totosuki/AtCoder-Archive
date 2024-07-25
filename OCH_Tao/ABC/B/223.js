const S = require("fs").readFileSync("/dev/stdin", "utf8").trim();
let L = [];
for (let i = 0; i < S.length; i++) {
  L.push(S.slice(i) + S.slice(0, i));
}
L.sort();
console.log(L[0]);
console.log(L[L.length - 1]);