const [S, T] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
let cnt = 0;
for (let a = 0; a < S + 1; a++) {
  for (let b = 0; b < S - a + 1; b++) {
    for (let c = 0; c < S - a - b + 1; c++) {
      if (a * b * c <= T) {
        cnt++;
      }
    }
  }
}
console.log(cnt);