const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [H, W] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
let S = [];
for (let i = 0; i < H; i++) {
  S.push([...input[i]]);
}
for (let i = 0; i < H; i++) {
  let l = [];
  for (let j = 0; j < W; j++) {
    if (S[i][j] === "#") {
      l.push("#");
    } else {
      let cnt = 0;
      if (i > 0 && j > 0) {
        if (S[i - 1][j - 1] === "#") {
          cnt++;
        }
      }
      if (i > 0) {
        if (S[i - 1][j] === "#") {
          cnt++;
        }
      }
      if (i > 0 && j < W - 1) {
        if (S[i - 1][j + 1] === "#") {
          cnt++;
        }
      }
      if (j > 0) {
        if (S[i][j - 1] === "#") {
          cnt++;
        }
      }
      if (j < W - 1) {
        if (S[i][j + 1] === "#") {
          cnt++;
        }
      }
      if (i < H - 1 && j > 0) {
        if (S[i + 1][j - 1] === "#") {
          cnt++;
        }
      }
      if (i < H - 1) {
        if (S[i + 1][j] === "#") {
          cnt++;
        }
      }
      if (i < H - 1 && j < W - 1) {
        if (S[i + 1][j + 1] === "#") {
          cnt++;
        }
      }
      l.push(String(cnt));
    }
  }
  console.log(l.join(""));
}