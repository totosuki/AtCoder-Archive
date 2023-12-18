const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]
if (input[0] === input[1] && input[1] === input[2] && input[2] === input[3]) {
  console.log("SAME");
} else {
  console.log("DIFFERENT");
}