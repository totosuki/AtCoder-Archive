const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
if (input[5] < input[4] - input[0]) {
  console.log(":(");
} else {
  console.log("Yay!");
}