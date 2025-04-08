const A = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(x => parseInt(x, 10));
loop: {
  for (let i = 0; i < A.length - 2; i++) {
    for (let j = i + 1; j < A.length - 1; j++) {
      for (let k = j + 1; k < A.length; k++) {
        if (A[i] + A[j] + A[k] === 1000) {
          console.log("Yes");
          break loop;
        }
      }
    }
  }
  console.log("No");
}