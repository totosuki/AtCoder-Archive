const [S, T] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
let cnt = 0;
for (let i = 0; i < S.length; i++) {
  if (S[i] !== T[i]) {
    cnt++;
  }
}
console.log(cnt);