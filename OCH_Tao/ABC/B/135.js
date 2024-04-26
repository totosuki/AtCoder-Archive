const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const P = (input[1].split(" ")).map(x => parseInt(x, 10));
const X = [...Array(N + 1).keys()].slice(1);
let flag = false;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    let L = [...P];
    [L[i], L[j]] = [L[j], L[i]];
    for (let k = 0; k < N; k++) {
      if (L[k] !== X[k]) {
        break;
      }
      if (k === N - 1) {
        flag = true;
      }
    }
  }
}
if (flag) {
  console.log("YES");
} else {
  console.log("NO");
}