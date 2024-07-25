const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
const X = [...S].reverse().join("");
let cnt = 0;
for (let i = 0; i < S.length; i++) {
  if (S[i] !== X[i]) {
    cnt++;
  }
}
console.log(cnt / 2);