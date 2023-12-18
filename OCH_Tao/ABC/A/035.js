const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(str => parseInt(str, 10));
if (input[0] / input[1] === 4 / 3) {
  console.log("4:3");
} else {
  console.log("16:9");
}