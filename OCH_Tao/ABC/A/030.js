const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(str => parseInt(str, 10));
if (input[1] / input[0] === input[3] / input[2]) {
  console.log("DRAW");
} else if (input[1] / input[0] > input[3] / input[2]) {
  console.log("TAKAHASHI");
} else {
  console.log("AOKI");
}