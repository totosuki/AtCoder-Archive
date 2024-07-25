const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [H, W] = input.shift().split(" ").map(x => parseInt(x, 10));
let A = [];
for (const i of input) {
  A.push(i.split(" ").map(x => parseInt(x, 10)));
}
for (let i1 = 0; i1 < H - 1; i1++) {
  for (let i2 = i1 + 1; i2 < H; i2++) {
    for (let j1 = 0; j1 < W - 1; j1++) {
      for (let j2 = j1 + 1; j2 < W; j2++) {
        if (A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]) {
          console.log("No");
          process.exit();
        }
      }
    }
  }
}
console.log("Yes");