const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
input.shift();
let X = 0;
let H = 0;
for (const i of input) {
  const [A, B] = i.split(" ").map(x => parseInt(x, 10));
  H = Math.max(H, B - A);
  X += A;
}
console.log(X + H);