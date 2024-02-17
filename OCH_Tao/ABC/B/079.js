const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
let L = [2n, 1n];
for (let i = 1; i < N; i++) {
  L.push(L[i - 1] + L[i]);
}
console.log((L[L.length - 1]).toString());