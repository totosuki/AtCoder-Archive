const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
const A = input[1].split(" ").map(x => parseInt(x, 10));
let L = [];
for (let i = 0; i < N; i++) {
  L.push(A[i]);
  while (L.length > 1) {
    if (L[L.length - 2] !== L[L.length - 1]) {
      break;
    } else {
      const X = L.pop();
      L.pop();
      L.push(X + 1);
    }
  }
}
console.log(L.length);