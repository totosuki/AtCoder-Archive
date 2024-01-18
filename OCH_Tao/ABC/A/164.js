const [S, W] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (S <= W) {
  console.log("unsafe");
} else {
  console.log("safe");
}