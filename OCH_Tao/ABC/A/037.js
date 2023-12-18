const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(str => parseInt(str, 10));
if (input[0] < input[1]) {
  console.log(Math.trunc(input[2] / input[0]));
} else {
  console.log(Math.trunc(input[2] / input[1]));
}