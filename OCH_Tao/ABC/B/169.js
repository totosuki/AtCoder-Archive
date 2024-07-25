const A = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(BigInt);
let cnt = 1n;
if (A.includes(0n)) {
  console.log(0);
  return false;
}
for (const i of A) {
  cnt *= i;
  if (cnt > 1e18) {
    console.log(-1);
    return false;
  }
}
console.log(cnt.toString());