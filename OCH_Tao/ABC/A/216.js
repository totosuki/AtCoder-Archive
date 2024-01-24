const [X, Y] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(".")).map(x => parseInt(x, 10));
if (0 <= Y && Y <= 2) {
  console.log(`${X}-`);
} else if (3 <= Y && Y <= 6) {
  console.log(X);
} else {
  console.log(`${X}+`);
}