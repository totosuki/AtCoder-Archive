const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input[0], 10);
const binN = N.toString(2);
const binNList = [...binN];
const NDigit = binNList.length;
let count = 0;
for (let i = 0; i < NDigit; i++) {
  if (binNList[i] === "1") {
    count++;
  }
}
console.log(count);
for (let i = NDigit; i > 0; i--) {
  if (binNList[i - 1] === "1") {
    console.log(2 ** (NDigit - i));
  }
}