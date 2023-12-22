const X = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (X[0] * X[1] >= X[2] * X[3]) {
  console.log(X[0] * X[1]);
} else {
  console.log(X[2] * X[3]);
}