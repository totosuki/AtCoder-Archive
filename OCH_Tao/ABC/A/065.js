const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (input[1] - input[2] >= 0) {
  console.log("delicious");
} else if (input[0] - (input[2] - input[1]) >= 0) {
  console.log("safe");
} else {
  console.log("dangerous");
}