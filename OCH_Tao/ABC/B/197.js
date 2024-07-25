const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [H, W, X, Y] = input.shift().split(" ").map(x => parseInt(x, 10));
let cnt = -3;
for (let i = X - 1; i < H; i++) {
  if (input[i][Y - 1] === "#") {
    break;
  } else {
    cnt++;
  }
}
for (let i = X - 1; i >= 0; i--) {
  if (input[i][Y - 1] === "#") {
    break;
  } else {
    cnt++;
  }
}
for (let i = Y - 1; i < W; i++) {
  if (input[X - 1][i] === "#") {
    break;
  } else {
    cnt++;
  }
}
for (let i = Y - 1; i >= 0; i--) {
  if (input[X - 1][i] === "#") {
    break;
  } else {
    cnt++;
  }
}
console.log(cnt);