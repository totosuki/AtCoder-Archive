const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = S.shift();
let l = [];
for (let i = 0; i < N; i++) {
  let x = S[i];
  let cnt = 0;
  for (let j = 0; j < N; j++) {
    if (x === S[j]) {
      cnt++;
    }
  }
  l.push(cnt);
}
let y = l.indexOf(Math.max(...l));
console.log(S[y]);