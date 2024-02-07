let [N, M, X, T, D] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (M >= X) {
  console.log(T);
} else {
  for (let i = X; i > M; i--) {
    T -= D;
  }
  console.log(T);
}