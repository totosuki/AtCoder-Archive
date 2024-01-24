const S = [...(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]];
let x = S[0];
let cnt = 0;
let l = [];
for (let i = 0; i < S.length; i++) {
  if (S[i] !== x) {
    l.push(x + String(cnt));
    x = S[i];
    cnt = 1;
  } else {
    cnt++;
  }
}
l.push(x + String(cnt));
console.log(l.join(""));