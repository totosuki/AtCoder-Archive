const [S, T] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
let cnt = 0;
for (let i = 0; i < 3; i++) {
  if (S[i] === T[i]) {
    cnt++;
  }
}
console.log(cnt);