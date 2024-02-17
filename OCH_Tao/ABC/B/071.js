const S = [...(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]];
let l = [...Array(26)].map((x, i) => String.fromCharCode(97 + i));
for (let i = 0; i < S.length; i++) {
  l = l.filter(x => x !== S[i]);
}
if (l.length > 0) {
  console.log(l[0]);
} else {
  console.log("None");
}