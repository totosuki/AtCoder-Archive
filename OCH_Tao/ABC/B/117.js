const L = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[1].split(" ")).map(x => parseInt(x, 10));
if (Math.max(...L) < L.reduce((a, b) => a + b) - Math.max(...L)) {
  console.log("Yes");
} else {
  console.log("No");
}