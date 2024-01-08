const [A, B, C] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
const X = C - (A - B);
if (X < 0) {
  console.log(0);
} else {
  console.log(X);
}