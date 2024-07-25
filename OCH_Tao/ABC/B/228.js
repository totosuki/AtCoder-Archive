const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, X] = input[0].split(" ").map(x => parseInt(x, 10));
let L = new Array(N).fill(0);
L[X - 1] = 1;
const A = input[1].split(" ").map(x => parseInt(x, 10));
let cnt = X;
while (true) {
  cnt = A[cnt - 1];
  if (L[cnt - 1] != 1) {
    L[cnt - 1] = 1;
  } else {
    break;
  }
}
console.log(L.reduce((a, b) => a + b, 0));