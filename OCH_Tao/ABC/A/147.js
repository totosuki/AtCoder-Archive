const A = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
const X = A[0] + A[1] + A[2];
if (X < 22) {
  console.log("win");
} else {
  console.log("bust");
}