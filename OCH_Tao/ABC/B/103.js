const [S, T] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
let flag = true;
for (let i = 0; i < S.length; i++) {
  const X = S.slice(i) + S.slice(0, i);
  if (X === T) {
    console.log("Yes");
    flag = false;
    break;
  }
}
if (flag) {
  console.log("No");
}