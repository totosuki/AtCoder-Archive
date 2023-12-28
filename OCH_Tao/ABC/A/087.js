const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
let x = input[0];
x -= input[1];

while (input[2] <= x) {
  x -= input[2];
}
console.log(x);