const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(str => parseInt(str, 10));
if (input[0] + input[1] === input[2] || input[1] + input[2] === input[0] || input[2] + input[0] === input[1]) {
  console.log("Yes");
} else {
  console.log("No");
}