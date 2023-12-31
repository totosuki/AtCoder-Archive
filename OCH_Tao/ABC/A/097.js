const [A, B, C, D] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (Math.abs(A - C) <= D) {
  console.log("Yes");
} else if (Math.abs(A - B) <= D && Math.abs(B - C) <= D) {
  console.log("Yes");
} else {
  console.log("No");
}