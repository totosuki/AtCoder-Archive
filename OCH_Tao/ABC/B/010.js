const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
const A = (input[1].split(" ")).map(x => parseInt(x, 10));
let cnt = 0;
for (let i = 0; i < N; i++) {
  let x = A[i];
  while (x % 2 === 0 || x % 3 === 2) {
    cnt++;
    x--;
  }
}
console.log(cnt);