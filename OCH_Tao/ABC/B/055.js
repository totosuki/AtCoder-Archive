const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
let p = 1;
for (let i = 1; i < N + 1; i++) {
  p *= i;
  p %= 1e9 + 7;
}
console.log(p);