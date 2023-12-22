const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let n = input[0] + input[1];
if (n >= 24) {
  console.log(n - 24);
} else {
  console.log(n);
}