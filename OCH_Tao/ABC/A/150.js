const [K, X] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (500 * K >= X) {
  console.log("Yes");
} else {
  console.log("No");
}