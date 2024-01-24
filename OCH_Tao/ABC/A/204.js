const [X, Y] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (X === Y) {
  console.log(X);
} else {
  console.log(3 - X - Y);
}