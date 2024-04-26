const N = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0], 10);
const divisor = x => {
  let count = 0;
  for (let i = 1; i < x + 1; i++) {
    if (x % i === 0) {
      count++;
    }
  }
  return count;
}
let cnt = 0;
for (let i = 1; i < N + 1; i += 2) {
  if (divisor(i) === 8) {
    cnt++;
  }
}
console.log(cnt);