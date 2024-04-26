const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [N, D] = input[0].split(" ").map(x => parseInt(x, 10));
const T = input[1].split(" ").map(x => parseInt(x, 10));
let flag = true;
for (let i = 1; i < N; i++) {
  if (T[i] - T[i - 1] <= D) {
    console.log(T[i]);
    flag = false;
    break;
  }
}
if (flag) {
  console.log(-1);
}