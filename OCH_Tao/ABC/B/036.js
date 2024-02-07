const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input.shift(), 10);
const rotate = a => a[0].map((_, c) => a.map(r => r[c]).reverse());
let l = [];
for (let i = 0; i < N; i++) {
  l.push([...input[i]]);
}
let rotL = rotate(l);
for (let i = 0; i < N; i++) {
  console.log([...rotL[i]].join(""));
}