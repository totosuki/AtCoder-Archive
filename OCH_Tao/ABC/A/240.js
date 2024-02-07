const [A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (Math.abs(A - B) === 1) {
  console.log("Yes");
} else if (Math.abs(A - B) === 9) {
  console.log("Yes");
} else {
  console.log("No");
}