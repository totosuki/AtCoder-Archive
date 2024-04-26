const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input.shift(), 10);
const S = [];
for (let i = 0; i < N; i++) {
  S.push(input.shift());
}
const M = parseInt(input.shift(), 10);
const T = [];
for (let i = 0; i < M; i++) {
  T.push(input.shift());
}
const union = (a, b) => {
  let A = new Set(a);
  let B = new Set(b);
  for (const i of B) {
    A.add(i);
  }
  return A;
}
const L = [...union(S, T)];
let x = 0;
for (const i of L) {
  let cnt = 0;
  for (const A of S) {
    if (i === A) {
      cnt++;
    }
  }
  for (const B of T) {
    if (i === B) {
      cnt--;
    }
  }
  x = Math.max(x, cnt);
}
console.log(x);