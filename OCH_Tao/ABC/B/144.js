const N = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0], 10);
let S = new Set();
for (let i = 1; i < 10; i++) {
  for (let j = 1; j < 10; j++) {
    S.add(i * j);
  }
}
console.log(S.has(N) ? "Yes" : "No");