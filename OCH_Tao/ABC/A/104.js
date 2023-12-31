const R = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (R < 1200) {
  console.log("ABC");
} else if (R < 2800) {
  console.log("ARC");
} else {
  console.log("AGC");
}