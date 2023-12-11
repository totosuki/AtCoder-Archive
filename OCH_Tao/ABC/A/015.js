const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const A = input[0];
const B = input[1];
if (A.length > B.length) {
  console.log(A);
} else {
  console.log(B);
}