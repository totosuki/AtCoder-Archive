const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N,] = input.shift().split(" ").map(x => parseInt(x, 10));
let L = Array(N).fill(true);
for (const i of input) {
  const [A, B] = i.split(" ");
  if (B === "M" && L[parseInt(A, 10) - 1]) {
    console.log("Yes");
    L[parseInt(A, 10) - 1] = false;
  } else {
    console.log("No");
  }
}