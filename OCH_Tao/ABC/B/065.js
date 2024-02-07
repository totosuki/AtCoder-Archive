const A = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
const N = A.shift();
let tmp = 1;
let cnt = 0;
let flag = false;
for (let i = 0; i < N; i++) {
  cnt++;
  tmp = A[tmp - 1];
  if (tmp === 2) {
    flag = true;
    break;
  }
}
if (flag) {
  console.log(cnt);
} else {
  console.log(-1);
}