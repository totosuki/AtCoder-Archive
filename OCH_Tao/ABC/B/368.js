const A = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(x => parseInt(x, 10));
let cnt = 0;
while (true) {
  cnt++;
  A.sort((a, b) => b - a);
  A[0]--;
  A[1]--;
  A.sort((a, b) => b - a);
  if (A[1] < 1) {
    console.log(cnt);
    break;
  }
}