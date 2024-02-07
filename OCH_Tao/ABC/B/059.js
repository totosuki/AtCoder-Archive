const [A, B] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(BigInt);
if (A > B) {
  console.log("GREATER");
} else if (A < B) {
  console.log("LESS");
} else {
  console.log("EQUAL");
}