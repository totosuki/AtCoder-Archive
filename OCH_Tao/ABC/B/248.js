let [A, B, K] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
let cnt = 0;
while (true) {
  if (A >= B) {
    console.log(cnt);
    break;
  } else {
    cnt++;
    A *= K;
  }
}