const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [, P, Q, R, S] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ");
const X = Q - P;
for (let i = -1; i < X; i++) {
  [A[P + i], A[R + i]] = [A[R + i], A[P + i]];
}
console.log(A.join(" "));