const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, X, Y, Z] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ").map(x => parseInt(x, 10));
const B = input[2].split(" ").map(x => parseInt(x, 10));
let C = [];
for (let i = 0; i < N; i++) {
  C.push({ "A": A[i], "B": B[i], "N": i + 1 });
}
let ans = [];
C.sort((a, b) => b.A - a.A || a.N - b.N);
for (const _ of Array(X)) {
  ans.push(C.shift().N);
}
C.sort((a, b) => b.B - a.B || a.N - b.N);
for (const _ of Array(Y)) {
  ans.push(C.shift().N);
}
C.sort((a, b) => (b.A + b.B) - (a.A + a.B) || a.N - b.N);
for (const _ of Array(Z)) {
  ans.push(C.shift().N);
}
console.log(ans.sort((a, b) => a - b).join("\n"));