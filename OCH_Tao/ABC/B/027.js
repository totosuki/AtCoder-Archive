const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
const A = (input[1].split(" ")).map(x => parseInt(x, 10));
let cnt = 0;
if (A.reduce((x, y) => x + y) % N === 0) {
  const one = A.reduce((x, y) => x + y) / N;
  for (let i = 1; i < N; i++) {
    let l = A.slice(0, i);
    if (l.reduce((x, y) => x + y) !== one * i) {
      cnt++;
    }
  }
} else {
  cnt = -1;
}
console.log(cnt);