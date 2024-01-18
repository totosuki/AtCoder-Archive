const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [S, T] = input[0].split(" ");
const [A, B] = (input[1].split(" ")).map(x => parseInt(x, 10));
const U = input[2];
if (U === S) {
  console.log(`${A - 1} ${B}`);
} else {
  console.log(`${A} ${B - 1}`);
}