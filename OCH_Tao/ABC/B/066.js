const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
for (let i = 2; i < S.length; i += 2) {
  if (S.slice(0, (S.length - i) / 2) === S.slice((S.length - i) / 2, S.length - i)) {
    console.log(S.length - i);
    break;
  }
}