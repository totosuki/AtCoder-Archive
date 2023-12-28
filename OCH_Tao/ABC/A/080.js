const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (input[0] * input[1] <= input[2]) {
  console.log(input[0] * input[1]);
} else {
  console.log(input[2]);
}