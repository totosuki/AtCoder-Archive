const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const H = input[1].split(" ").map(x => parseInt(x, 10));
for (let i = 0; i < N; i++) {
  if (H[i] > H[0]) {
    console.log(i + 1);
    break;
  }
  if (i === N - 1) {
    console.log(-1);
  }
}