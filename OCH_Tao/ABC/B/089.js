const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const S = input[1].split(" ");
if ([...new Set(S)].length === 3) {
  console.log("Three");
} else {
  console.log("Four");
}