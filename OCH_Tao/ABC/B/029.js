const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
let cnt = 0;
for (let i = 0; i < 12; i++) {
  if (/r/.test(S[i])) {
    cnt++;
  }
}
console.log(cnt);