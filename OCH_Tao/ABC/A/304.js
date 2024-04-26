const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input.shift(), 10);
let X = [];
let Y = [];
let cnt;
for (const i of input) {
  const [A, B] = i.split(" ");
  X.push(A);
  Y.push(parseInt(B, 10));
  cnt = cnt === undefined ? parseInt(B) : Math.min(cnt, parseInt(B, 10));
}
let j = Y.indexOf(cnt);
console.log(X.slice(j).concat(X.slice(0, j)).join("\n"));