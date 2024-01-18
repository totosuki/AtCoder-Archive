const [A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (A + B >= 15 && B >= 8) {
  console.log(1);
} else if (A + B >= 10 && B >= 3) {
  console.log(2);
} else if (A + B >= 3) {
  console.log(3);
} else {
  console.log(4);
}