const [A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (B - A > 0) {
  console.log(B - A + 1);
} else {
  console.log(0);
}