const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const A = parseInt(input[0].split(" ")[1], 10);
const T = input[1].split(" ").map(x => parseInt(x, 10));
let cnt = 0;
for (const i of T) {
  if (cnt < i) {
    cnt = i;
  }
  cnt += A;
  console.log(cnt);
}