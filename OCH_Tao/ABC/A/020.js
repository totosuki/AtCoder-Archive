const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
if (input[0] === "1") {
  console.log("ABC");
} else {
  console.log("chokudai");
}