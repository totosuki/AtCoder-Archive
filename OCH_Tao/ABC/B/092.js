const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input.shift(), 10);
let [D, X] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
for (let i = 1; i < D + 1; i++) {
  for (const A of input) {
    const j = parseInt(A, 10);
    if (j === 1) {
      X++;
    } else if (i % j === 1) {
      X++;
    }
  }
}
console.log(X);