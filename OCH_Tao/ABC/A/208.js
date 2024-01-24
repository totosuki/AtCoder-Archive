const [A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (A <= B && B <= 6 * A) {
  console.log("Yes");
} else {
  console.log("No");
}