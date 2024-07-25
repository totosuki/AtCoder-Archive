const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift(), 10);
let D = [];
let sum = 0;
for (const i of input) {
  const [S, C] = i.split(" ");
  sum += parseInt(C, 10);
  D.push({ "S": S, "C": parseInt(C, 10) });
}
D.sort((a, b) => a.S < b.S ? -1 : 1);
console.log(D[sum % N].S);