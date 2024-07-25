const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
let M = parseInt(input[0].split(" ")[1], 10);
const H = input[1].split(" ").map(x => parseInt(x, 10));
let cnt = 0;
for (const i of H) {
  if (M >= i) {
    cnt++;
    M -= i;
  } else {
    break;
  }
}
console.log(cnt);