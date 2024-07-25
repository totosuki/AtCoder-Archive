const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
const D = input[1].split(" ").map(x => parseInt(x, 10));
let cnt = 0;
for (let i = 0; i < N - 1; i++) {
  for (let j = i + 1; j < N; j++) {
    cnt += D[i] * D[j];
  }
}
console.log(cnt);