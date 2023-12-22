const X = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (X >= 1200) {
  console.log("ARC");
} else {
  console.log("ABC");
}