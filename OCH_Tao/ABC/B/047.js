const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [W, H, N] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
let o = [0, 0];
let p = [W, H];
for (let i = 0; i < N; i++) {
  let [x, y, a] = (input[i].split(" ")).map(x => parseInt(x, 10));
  if (a === 1) {
    if (o[0] < x) {
      o[0] = x;
    }
  } else if (a === 2) {
    if (p[0] > x) {
      p[0] = x;
    }
  } else if (a === 3) {
    if (o[1] < y) {
      o[1] = y;
    }
  } else {
    if (p[1] > y) {
      p[1] = y;
    }
  }
}
if ((p[0] - o[0]) > 0 && (p[1] - o[1]) > 0) {
  console.log((p[0] - o[0]) * (p[1] - o[1]));
} else {
  console.log(0);
}