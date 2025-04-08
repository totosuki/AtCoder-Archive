const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
let X = Array(1509).fill([]).map(_ => Array(1509).fill(0));
for (let i = 1; i < N + 1; i++) {
  const [A, B, C, D] = input[i].split(" ").map(x => parseInt(x, 10));
  X[A + 1][B + 1]++;
  X[C + 1][D + 1]++;
  X[A + 1][D + 1]--;
  X[C + 1][B + 1]--;
}
for (let i = 1; i < 1509; i++) {
  for (let j = 1; j < 1509; j++) {
    X[i][j] += X[i][j - 1];
  }
}
for (let i = 1; i < 1509; i++) {
  for (let j = 1; j < 1509; j++) {
    X[j][i] += X[j - 1][i];
  }
}
let cnt = 0;
for (const i of X) {
  for (const j of i) {
    if (j > 0) {
      cnt++;
    }
  }
}
console.log(cnt);