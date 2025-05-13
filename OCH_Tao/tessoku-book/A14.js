const [[N, K], A, B, C, D] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n").map(x => x.split(" ").map(y => parseInt(y, 10)));
const P = new Set();
const Q = new Set();
for (const i of A) {
  for (const j of B) {
    P.add(i + j);
  }
}
for (const i of C) {
  for (const j of D) {
    Q.add(i + j);
  }
}
for (const i of P) {
  if (Q.has(K - i)) {
    console.log("Yes");
    process.exit();
  }
}
console.log("No");