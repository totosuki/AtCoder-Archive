const X = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (X < 0) {
  console.log(0);
} else {
  console.log(X);
}