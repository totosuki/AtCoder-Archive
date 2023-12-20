const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
const A = parseInt(input[0], 10);
const B = parseInt(input[2], 10);
if (input[1] === "+") {
  console.log(A + B);
} else {
  console.log(A - B);
}