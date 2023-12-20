const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(str => parseInt(str, 10));
if (input[0] - input[1] <= 0) {
  console.log(input[0] * input[2]);
} else {
  console.log(input[1] * input[2] + (input[0] - input[1]) * input[3]);
}