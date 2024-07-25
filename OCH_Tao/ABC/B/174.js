const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const D = parseInt(input.shift().split(" ")[1], 10) ** 2;
let cnt = 0;
for (const i of input) {
  const [X, Y] = i.split(" ").map(x => parseInt(x, 10));
  if (X ** 2 + Y ** 2 <= D) {
    cnt++;
  }
}
console.log(cnt);