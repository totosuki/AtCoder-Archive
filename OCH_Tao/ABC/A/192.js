X = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (X % 100 === 0) {
  console.log(100);
} else {
  console.log(100 - X % 100);
}