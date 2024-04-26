const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, M, C] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
const B = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
let cnt = 0;
for (const X of input) {
  const A = (X.split(" ")).map(x => parseInt(x, 10));
  let tmp = 0;
  for (let i = 0; i < M; i++) {
    tmp += A[i] * B[i];
  }
  tmp += C;
  if (tmp > 0) {
    cnt++;
  }
}
console.log(cnt);