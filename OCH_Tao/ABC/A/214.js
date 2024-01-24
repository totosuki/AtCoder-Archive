const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (N <= 125) {
  console.log(4);
} else if (N <= 211) {
  console.log(6);
} else {
  console.log(8);
}