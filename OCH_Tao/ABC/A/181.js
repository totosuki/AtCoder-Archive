const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (N % 2 === 0) {
  console.log("White");
} else {
  console.log("Black");
}