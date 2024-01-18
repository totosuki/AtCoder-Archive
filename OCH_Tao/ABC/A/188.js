const [X, Y] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (Math.abs(X - Y) < 3) {
  console.log("Yes");
} else {
  console.log("No");
}