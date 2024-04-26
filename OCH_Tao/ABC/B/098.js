const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const S = [...input[1]];
let cnt = 0;
const intersection = (a, b) => {
  const A = new Set(a);
  const B = new Set(b);
  const _intersection = new Set();
  for (const i of B) {
    if (A.has(i)) {
      _intersection.add(i)
    }
  }
  return _intersection;
}
for (let i = 0; i < N; i++) {
  let X = new Set(S.slice(0, i));
  let Y = new Set(S.slice(i));
  cnt = Math.max(cnt, [...intersection(X, Y)].length);
}
console.log(cnt);