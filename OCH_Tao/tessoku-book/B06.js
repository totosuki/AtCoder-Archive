const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
input.shift();
const A = input.shift().split(" ").map(x => parseInt(x, 10));
let X = [0];
for (const i of A) {
  X.push(X[X.length - 1] + i);
}
input.shift();
for (const i of input) {
  const [L, R] = i.split(" ").map(x => parseInt(x, 10));
  const Y = X[R] - X[L - 1];
  console.log(Y > (R - L + 1) - Y ? "win" : Y < (R - L + 1) - Y ? "lose" : "draw");
}