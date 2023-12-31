const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
let x = 0;
if (input[0] < input[1]) {
  x += input[0];
} else {
  x += input[1];
}
if (input[2] < input[3]) {
  x += input[2];
} else {
  x += input[3];
}
console.log(x);