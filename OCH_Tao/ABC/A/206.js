const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
const X = Math.floor(N * 1.08);
if (X < 206) {
  console.log("Yay!");
} else if (X === 206) {
  console.log("so-so");
} else {
  console.log(":(");
}