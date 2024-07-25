const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
input.shift();
let A = [];
for (const i of input) {
  A.push(...i.split(" ").map(x => parseInt(x, 10)));
}
console.log(A.map(x => x - Math.min(...A)).reduce((a, b) => a + b, 0));