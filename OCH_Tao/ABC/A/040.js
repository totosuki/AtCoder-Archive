const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(str => parseInt(str, 10));
const a = input[0] - input[1];
const b = input[1] - 1;
if (a < b) {
  console.log(a);
} else {
  console.log(b);
}