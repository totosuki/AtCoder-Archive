const [A, B, C] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (C === A + B && C === A - B) {
  console.log("?");
} else if (C === A + B) {
  console.log("+");
} else if (C === A - B) {
  console.log("-");
} else {
  console.log("!");
}