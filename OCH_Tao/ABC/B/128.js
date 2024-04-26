const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift(), 10);
const L = [];
let Y = new Set();
let i = 1;
for (const X of input) {
  const [S, P] = X.split(" ");
  Y.add(S);
  L.push([S, parseInt(P, 10), i]);
  i++;
}
let Z = [...Y];
Z.sort();
for (const X of Z) {
  let l = L.filter(x => x[0] === X);
  l.sort((a, b) => b[1] - a[1]);
  for (const i of l) {
    console.log(i[2]);
  }
}