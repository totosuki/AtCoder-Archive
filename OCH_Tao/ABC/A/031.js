const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
const A = parseInt(input[0], 10);
const D = parseInt(input[1], 10);
const upA = (A + 1) * D;
const upD = A * (D + 1);
if (upA >= upD) {
  console.log(upA);
} else {
  console.log(upD);
}