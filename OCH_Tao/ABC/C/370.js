let [S, T] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
let M = 0;
let diff = new Set();
for (let i = 0; i < S.length; i++) {
  if (S[i] !== T[i]) {
    M++;
    diff.add(i);
  }
}
console.log(M);
for (let i = 0; i < M; i++) {
  let tmp = [];
  for (const j of diff.values()) {
    tmp.push([S.slice(0, j) + T[j] + S.slice(j + 1), j]);
  }
  tmp.sort((a, b) => a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0);
  S = tmp[0][0];
  diff.delete(tmp[0][1]);
  console.log(S);
}