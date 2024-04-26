const S = [...(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]];
let cnt = {};
S.forEach(i => cnt[i] = (cnt[i] || 0) + 1);
for (const i in cnt) {
  if (cnt[i] === 1) {
    console.log(S.indexOf(i) + 1);
    break;
  }
}