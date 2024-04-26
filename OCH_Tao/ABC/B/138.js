const A = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(x => parseInt(x, 10));
let cnt = 0;
for (const i of A) {
  cnt += 1 / i;
}
console.log(1 / cnt);