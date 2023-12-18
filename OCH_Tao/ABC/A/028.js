const input = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (input === 100) {
  console.log("Perfect");
} else if (input >= 90) {
  console.log("Great");
} else if (input >= 60) {
  console.log("Good");
} else {
  console.log("Bad");
}