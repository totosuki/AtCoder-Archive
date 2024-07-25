const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
input.shift();
let ans = 0;
for (const i of input) {
  const [A, B] = i.split(" ").map(x => parseInt(x, 10));
  ans += (A + B) * (B - A + 1) / 2;
}
console.log(ans);