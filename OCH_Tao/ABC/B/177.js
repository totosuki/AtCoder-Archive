const [S, T] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
let ans = T.length;
for (let i = 0; i <= S.length - T.length; i++) {
  let cnt = 0;
  for (let j = 0; j < T.length; j++) {
    if (T[j] !== S[i + j]) {
      cnt++;
    }
  }
  ans = Math.min(ans, cnt);
}
console.log(ans);