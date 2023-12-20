const input = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
let x = 0;
for (let i = 0; i < input; i++) {
  x += i + 1;
}
console.log(x);