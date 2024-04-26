const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, M, X] = (input[0].split(" ")).map(x => parseInt(x, 10));
const A = (input[1].split(" ")).map(x => parseInt(x, 10));
let case0 = 0;
let caseN = 0;
for (let i = X; i > -1; i--) {
  if (A.includes(i)) {
    case0++;
  }
}
for (let i = X; i < N + 1; i++) {
  if (A.includes(i)) {
    caseN++;
  }
}
console.log(Math.min(case0, caseN));