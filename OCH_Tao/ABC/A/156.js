const [N, R] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (N >= 10) {
  console.log(R);
} else {
  console.log(R + (100 * (10 - N)));
}