const [N, A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (N * A < B) {
  console.log(N * A);
} else {
  console.log(B);
}