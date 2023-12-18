const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const ABCK = (input[0].split(" ")).map(str => parseInt(str, 10));
const ST = (input[1].split(" ")).map(str => parseInt(str, 10));
let x = ABCK[0] * ST[0] + ABCK[1] * ST[1];
if (ABCK[3] <= ST[0] + ST[1]) {
  x -= ABCK[2] * (ST[0] + ST[1]);
}
console.log(x);