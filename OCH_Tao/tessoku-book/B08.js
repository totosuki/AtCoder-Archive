const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
let L = Array(1509).fill([]).map(_ => Array(1509).fill(0));
for (let i = 1; i < N + 1; i++) {
  const [X, Y] = input[i].split(" ").map(x => parseInt(x, 10));
  L[X][Y]++;
}
for (let i = 1; i < 1501; i++) {
  for (let j = 1; j < 1501; j++) {
    L[i][j] += L[i][j - 1];
  }
}
for (let i = 1; i < 1501; i++) {
  for (let j = 1; j < 1501; j++) {
    L[j][i] += L[j - 1][i];
  }
}
const Q = parseInt(input[N + 1], 10);
for (let i = N + 2; i < N + Q + 2; i++) {
  const [A, B, C, D] = input[i].split(" ").map(x => parseInt(x, 10));
  console.log(L[C][D] + L[A - 1][B - 1] - L[A - 1][D] - L[C][B - 1]);
}