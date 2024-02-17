const [N, K] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
let l = [1];
for (let i = 0; i < N; i++) {
  let A = l.map(x => x * 2);
  let B = l.map(x => x + K);
  l = A.concat(B);
}
console.log(Math.min(...l));