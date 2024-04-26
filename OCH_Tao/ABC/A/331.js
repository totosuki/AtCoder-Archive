const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [M, D] = input[0].split(" ").map(x => parseInt(x, 10));
const [y, m, d] = input[1].split(" ").map(x => parseInt(x, 10));
if (M === m && D === d) {
  console.log(`${y + 1} 1 1`);
} else if (D === d) {
  console.log(`${y} ${m + 1} 1`);
} else {
  console.log(`${y} ${m} ${d + 1}`);
}