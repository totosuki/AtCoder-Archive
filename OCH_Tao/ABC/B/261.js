const A = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(A.shift(), 10);
for (let i = 0; i < N; i++) {
  for (let j = i; j < N; j++) {
    if (i === j) {
      continue;
    }
    if (A[i][j] === "W") {
      if (A[j][i] !== "L") {
        console.log("incorrect");
        process.exit();
      }
    }
    if (A[i][j] === "D") {
      if (A[j][i] !== "D") {
        console.log("incorrect");
        process.exit();
      }
    }
    if (A[i][j] === "L") {
      if (A[j][i] !== "W") {
        console.log("incorrect");
        process.exit();
      }
    }
  }
}
console.log("correct");