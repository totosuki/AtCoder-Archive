const [W, A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (Math.abs(A - B) <= W) {
  console.log(0);
} else {
  console.log(Math.abs(A - B) - W);
}