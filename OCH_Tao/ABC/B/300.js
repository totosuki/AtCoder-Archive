const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [H, W] = input.shift().split(" ").map(x => parseInt(x, 10));
const A = input.slice(0, H);
const B = input.slice(H);
for (let i = 0; i < H; i++) {
  for (let j = 0; j < W; j++) {
    check: {
      for (let x = 0; x < H; x++) {
        for (let y = 0; y < W; y++) {
          if (A[(x + i) % H][(y + j) % W] !== B[x][y]) {
            break check;
          }
        }
      }
      console.log("Yes");
      process.exit();
    }
  }
}
console.log("No");