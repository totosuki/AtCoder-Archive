const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
input.shift();
let A = input.shift().split(" ").map(x => parseInt(x, 10));
const Q = parseInt(input.shift(), 10);
for (let i = 0; i < Q; i++) {
  const [n, ...k] = input[i].split(" ").map(x => parseInt(x, 10));
  if (n === 1) {
    A[k[0] - 1] = k[1];
  } else {
    console.log(A[k[0] - 1]);
  }
}