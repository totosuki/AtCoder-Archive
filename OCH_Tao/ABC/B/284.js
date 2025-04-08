const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const T = parseInt(input.shift(), 10);
for (let i = 1; i < T * 2; i += 2) {
  const A = input[i].split(" ").map(x => parseInt(x, 10));
  console.log(A.filter(x => x % 2 === 1).length);
}