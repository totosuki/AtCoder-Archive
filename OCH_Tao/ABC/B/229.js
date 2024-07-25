const [A, B] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => [...x].reverse());
for (let i = 0; i < Math.min(A.length, B.length); i++) {
  if (parseInt(A[i], 10) + parseInt(B[i], 10) > 9) {
    console.log("Hard");
    process.exit();
  }
}
console.log("Easy");