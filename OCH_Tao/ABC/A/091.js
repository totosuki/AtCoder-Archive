const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (input[0] + input[1] >= input[2]) {
  console.log("Yes");
} else {
  console.log("No");
}