const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
let [N, , T] = input.shift().split(" ").map(x => parseInt(x, 10));
const A = input.shift().split(" ").map(x => parseInt(x, 10));
let D = new Map();
for (const i of input) {
  const [X, Y] = i.split(" ").map(x => parseInt(x, 10));
  D.set(X, Y);
}
for (let i = 1; i < N; i++) {
  T += (D.get(i) ?? 0);
  T -= A[i - 1];
  if (T <= 0) {
    console.log("No");
    process.exit();
  }
}
console.log("Yes");