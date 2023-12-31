const [N, K] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (N % K === 0) {
  console.log(0);
} else {
  console.log(1);
}