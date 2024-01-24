const [N, A, X, Y] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (N <= A) {
  console.log(N * X);
} else {
  console.log(A * X + (N - A) * Y);
}