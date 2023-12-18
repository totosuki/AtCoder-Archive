const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const NST = ((input.splice(0, 1))[0].split(" ")).map(str => parseInt(str, 10));
const A = input.map(str => parseInt(str, 10));
let l = [];
let now = 0;
for (let i = 0; i < NST[0]; i++) {
  now += A[i];
  l.push(now);
}
let cnt = 0;
for (let i = 0; i < l.length; i++) {
  if (NST[1] <= l[i] && l[i] <= NST[2]) {
    cnt++;
  }
}
console.log(cnt);