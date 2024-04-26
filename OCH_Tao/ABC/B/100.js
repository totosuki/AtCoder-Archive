const [D, N] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (N < 100) {
  console.log((100 ** D) * N);
} else {
  console.log((100 ** D) * (N + 1));
}