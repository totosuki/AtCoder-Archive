const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(str => parseInt(str, 10));
let x = input[0];
for (let i = 1; x % input[1] > 0 || x < input[2]; i++) {
  x = input[0] * i;
}
console.log(x);