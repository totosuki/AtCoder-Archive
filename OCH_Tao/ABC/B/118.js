const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, M] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
let cnt = new Array(M);
cnt.fill(0);
for (const X of input) {
  let A = (X.split(" ")).map(x => parseInt(x, 10));
  const K = parseInt(A.shift(), 10);
  for (const Y of A) {
    cnt[Y - 1]++;
  }
}
let A = 0;
for (const Z of cnt) {
  if (Z === N) {
    A++;
  }
}
console.log(A);