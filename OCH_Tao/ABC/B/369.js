const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
input.shift();
let [L, R, cnt] = [0, 0, 0];
for (const i of input) {
  let [A, S] = i.split(" ");
  A = parseInt(A, 10);
  if (S === "L") {
    if (L !== 0) {
      cnt += Math.abs(L - A);
    }
    L = A;
  } else {
    if (R !== 0) {
      cnt += Math.abs(R - A);
    }
    R = A;
  }
}
console.log(cnt);