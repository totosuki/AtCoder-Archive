const [A, B] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
let x = Math.abs(A - B);
if (x < 10 - x) {
  console.log(x);
} else {
  console.log(10 - x);
}