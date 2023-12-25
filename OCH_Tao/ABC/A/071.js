const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (Math.abs(input[0] - input[1]) < Math.abs(input[0] - input[2])) {
  console.log("A");
} else {
  console.log("B");
}