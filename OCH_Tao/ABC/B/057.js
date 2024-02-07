const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [N, M] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
let s = [];
for (let i = 0; i < N; i++) {
  s.push(((input.shift()).split(" ")).map(x => parseInt(x, 10)));
}
let c = [];
for (let i = 0; i < M; i++) {
  c.push(((input.shift()).split(" ")).map(x => parseInt(x, 10)));
}
for (let i = 0; i < N; i++) {
  let l = [];
  for (let j = 0; j < M; j++) {
    l.push(Math.abs(s[i][0] - c[j][0]) + Math.abs(s[i][1] - c[j][1]));
  }
  console.log(l.indexOf(Math.min(...l)) + 1);
}