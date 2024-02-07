const [S, input] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const K = parseInt(input, 10);
let l = [];
if (S.length < K) {
  console.log(0);
} else {
  for (let i = 0; i < S.length; i++) {
    l.push(S.slice(i, i + K));
  }
  let able = [...new Set(l.filter((x) => x.length === K))];
  console.log(able.length);
}