const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (N < 1000) {
  console.log("ABC");
} else {
  console.log("ABD");
}