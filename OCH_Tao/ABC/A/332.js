const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [, S, K] = input.shift().split(" ").map(x => parseInt(x, 10));
let cnt = 0;
for (const i of input) {
  const [P, Q] = i.split(" ").map(x => parseInt(x, 10));
  cnt += P * Q;
}
console.log(cnt >= S ? cnt : cnt + K);