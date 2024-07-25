const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const L = input[1].split(" ").map(x => parseInt(x, 10));
let cnt = 0;
for (let i = 0; i < N; i++) {
  for (let j = i + 1; j < N; j++) {
    for (let k = j + 1; k < N; k++) {
      if (L[i] !== L[j] && L[j] !== L[k] && L[k] !== L[i]) {
        if (Math.max(L[i], L[j], L[k]) < L[i] + L[j] + L[k] - Math.max(L[i], L[j], L[k])) {
          cnt++;
        }
      }
    }
  }
}
console.log(cnt);