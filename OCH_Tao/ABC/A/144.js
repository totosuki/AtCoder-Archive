const [A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (A < 10 && B < 10) {
  console.log(A * B);
} else {
  console.log(-1);
}