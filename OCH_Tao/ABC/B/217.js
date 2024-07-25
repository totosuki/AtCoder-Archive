const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const X = ["ABC", "ARC", "AGC", "AHC"];
for (const i of X) {
  if (!S.includes(i)) {
    console.log(i);
    break;
  }
}