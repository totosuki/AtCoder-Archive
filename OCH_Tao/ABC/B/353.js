const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const K = parseInt(input[0].split(" ")[1], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
let tmp = 0;
let cnt = 0;
for (const i of A) {
  if (K - tmp < i) {
    cnt++;
    tmp = 0;
  }
  tmp += i;
}
console.log(cnt + 1);