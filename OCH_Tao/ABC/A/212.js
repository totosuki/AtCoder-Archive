const [A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (A > 0 && B === 0) {
  console.log("Gold");
} else if (A === 0 && B > 0) {
  console.log("Silver");
} else {
  console.log("Alloy");
}