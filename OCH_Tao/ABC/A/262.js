let Y = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
while (Y % 4 !== 2) {
  Y++;
}
console.log(Y);