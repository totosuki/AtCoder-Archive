const [A, B, C, X] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (X <= A) {
  console.log(1);
} else if (B < X) {
  console.log(0);
} else {
  console.log(C / (B - A));
}