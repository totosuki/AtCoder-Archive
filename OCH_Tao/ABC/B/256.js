const A = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(x => parseInt(x, 10));
let X = Array(4).fill(0);
let cnt = 0;
for (const i of A) {
  X[0] = 1;
  for (let j = 0; j < i; j++) {
    cnt += X.pop();
    X.unshift(0);
  }
}
console.log(cnt);