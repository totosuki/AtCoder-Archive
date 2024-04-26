const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
const P = input[1].split(" ").map(x => parseInt(x, 10));
if (N === 1) {
  console.log(0);
} else {
  if (P[0] > Math.max(...P.slice(1))) {
    console.log(0);
  } else {
    console.log(Math.max(...P.slice(1)) - P[0] + 1);
  }
}