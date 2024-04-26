const [, ...input] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
let T = 0;
let A = 0;
for (const i of input) {
  const [X, Y] = i.split(" ").map(x => parseInt(x, 10));
  T += X;
  A += Y;
}
console.log(T > A ? "Takahashi" : T < A ? "Aoki" : "Draw");