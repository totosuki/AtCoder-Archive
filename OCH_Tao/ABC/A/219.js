const X = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (X >= 90) {
  console.log("expert");
} else if (X >= 70) {
  console.log(90 - X);
} else if (X >= 40) {
  console.log(70 - X);
} else {
  console.log(40 - X);
}