let [A, B, C, D] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0].split(" ").map(x => parseInt(x, 10));
while (true) {
  C -= B;
  if (C < 1) {
    break;
  }
  A -= D;
  if (A < 1) {
    break;
  }
}
console.log(C < A ? "Yes" : "No");