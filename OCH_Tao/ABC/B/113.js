const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [T, A] = (input[1].split(" ")).map(x => parseInt(x, 10));
const H = (input[2].split(" ")).map(x => parseInt(x, 10));
let L = [];
for (const X of H) {
  L.push(Math.abs(A - (T - X * 0.006)));
}
console.log(L.indexOf(Math.min(...L)) + 1);