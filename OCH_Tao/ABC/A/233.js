const [X, Y] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (X >= Y) {
  console.log(0);
} else {
  console.log(Math.ceil((Y - X) / 10));
}