const [A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (A > 8 || B > 8) {
  console.log(":(");
} else {
  console.log("Yay!");
}