const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift(), 10);
let A = input.slice(0, N).map(x => x.split(" "));
const B = input.slice(N).map(x => x.split(" "));
for (let i = 0; i < 4; i++) {
  checkArray: {
    for (let x = 0; x < N; x++) {
      for (let y = 0; y < N; y++) {
        if (A[x][y] === "1" && B[x][y] === "0") {
          break checkArray;
        }
      }
    }
    console.log("Yes");
    process.exit();
  }
  A = A[0].map((_, c) => A.map(r => r[c])).reverse();
}
console.log("No");