const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, , T] = input.shift().split(" ").map(x => parseInt(x, 10));
let cnt = N;
let X = 0;
for (const i of input) {
  const [A, B] = i.split(" ").map(x => parseInt(x, 10));
  cnt = Math.max(0, cnt - (A - X));
  if (cnt > 0) {
    cnt = Math.min(N, cnt + (B - A));
    X = B;
  } else {
    console.log("No");
    return false;
  }
}
cnt = Math.max(0, cnt - (T - X));
console.log(cnt > 0 ? "Yes" : "No");