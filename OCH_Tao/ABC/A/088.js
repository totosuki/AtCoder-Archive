const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
let n = input[0];
while (500 <= n) {
  n -= 500;
}
if (n <= input[1]) {
  console.log("Yes");
} else {
  console.log("No");
}