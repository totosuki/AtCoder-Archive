const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const A = parseInt(input[0], 10);
const B = parseInt(input[1], 10);
if (A % B === 0) {
  console.log(0);
} else {
  console.log(B - (A % B));
}