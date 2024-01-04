const [A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (A <= 5) {
  console.log(0);
} else if (A <= 12) {
  console.log(Math.trunc(B / 2));
} else {
  console.log(B);
}