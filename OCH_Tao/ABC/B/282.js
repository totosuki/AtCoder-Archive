const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, M] = input.shift().split(" ").map(x => parseInt(x, 10));
const S = input.map(x => parseInt(x.replaceAll("o", "1").replaceAll("x", "0"), 2));
let cnt = 0;
for (let i = 0; i < N - 1; i++) {
  for (let j = i + 1; j < N; j++) {
    if ((S[i] | S[j]) === parseInt("1".repeat(M), 2)) {
      cnt++;
    }
  }
}
console.log(cnt);