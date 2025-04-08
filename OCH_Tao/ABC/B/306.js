/*
const A = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
let cnt = 0n;
for (const [i, j] of A.entries()) {
  cnt += 2n ** BigInt(i) * BigInt(j);
}
console.log(cnt.toString());
*/

console.log(BigInt("0b" + require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").reverse().join("")).toString());