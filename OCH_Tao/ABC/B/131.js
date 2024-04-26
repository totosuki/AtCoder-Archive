const [N, L] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let X = [];
for (let i = L; i < L + N; i++) {
  X.push(i);
}
X.sort((a, b) => Math.abs(a) - Math.abs(b));
console.log(X.slice(1).reduce((a, b) => a + b, 0));