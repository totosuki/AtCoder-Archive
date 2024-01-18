const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
const X = N % 1000;
if (X === 0) {
  console.log(X);
} else {
  console.log(1000 - X);
}