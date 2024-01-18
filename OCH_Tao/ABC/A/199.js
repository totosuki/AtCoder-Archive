const [A, B, C] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (A ** 2 + B ** 2 < C ** 2) {
  console.log("Yes");
} else {
  console.log("No");
}