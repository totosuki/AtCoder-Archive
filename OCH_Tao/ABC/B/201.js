const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n").slice(1);
let L = [];
for (const i of input) {
  const [S, T] = i.split(" ");
  L.push({ "S": S, "T": parseInt(T, 10) });
}
L.sort((a, b) => b.T - a.T);
console.log(L[1].S);