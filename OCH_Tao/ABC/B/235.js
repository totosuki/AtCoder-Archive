const H = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(x => parseInt(x, 10));
let ans = 0;
for (const i of H) {
  if (i > ans) {
    ans = i;
  } else {
    break;
  }
}
console.log(ans);