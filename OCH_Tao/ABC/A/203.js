const [A, B, C] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (A === B) {
  console.log(C);
} else if (B === C) {
  console.log(A);
} else if (C === A) {
  console.log(B);
} else {
  console.log(0);
}