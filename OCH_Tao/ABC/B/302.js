const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [H, W] = input.shift().split(" ").map(x => parseInt(x, 10));
const S = input.map(x => [...x]);
const D = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];
for (let i = 0; i < H; i++) {
  for (let j = 0; j < W; j++) {
    if (S[i][j] === "s") {
      let str = "";
      for (const [x, y] of D) {
        for (let n = 0; n < 5; n++) {
          if (0 <= i + x * n && i + x * n < H && 0 <= j + y * n && j + y * n < W) {
            str += S[i + x * n][j + y * n];
          } else {
            break;
          }
        }
        if (str === "snuke") {
          for (let n = 0; n < 5; n++) {
            console.log([i + x * n + 1, j + y * n + 1].join(" "));
          }
          process.exit();
        } else {
          str = "";
        }
      }
    }
  }
}