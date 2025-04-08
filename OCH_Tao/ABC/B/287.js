const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, M] = input.shift().split(" ").map(x => parseInt(x, 10));
const S = input.splice(0, N);
const T = new Set(input);
let cnt = 0;
for (const i of S) {
  if (T.has(i.slice(3))) {
    cnt++;
  }
}
console.log(cnt);