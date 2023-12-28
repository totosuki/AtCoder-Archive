const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
const L = input[0] + input[1];
const R = input[2] + input[3];
if (L === R) {
  console.log("Balanced");
} else if (L > R) {
  console.log("Left");
} else {
  console.log("Right");
}