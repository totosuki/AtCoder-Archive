const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
let cnt = 0;
for (let i = 0; i < S.length; i++) {
  if (S[i] === "w") {
    cnt += 2;
  } else {
    cnt++;
  }
}
console.log(cnt);