const [A, B, K] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let L = [];
for (let i = 1; i < Math.max(A, B) + 1; i++) {
  if (A % i === 0 && B % i === 0) {
    L.push(i);
  }
}
L.reverse();
console.log(L[K - 1]);