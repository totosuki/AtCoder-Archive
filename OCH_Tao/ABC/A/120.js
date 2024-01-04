const [A, B, C] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (Math.trunc(B / A) > C) {
  console.log(C);
} else {
  console.log(Math.trunc(B / A));
}