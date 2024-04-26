const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift(), 10);
let cnt = 0;
for (const A of input) {
  const [X, U] = A.split(" ");
  if (U === "BTC") {
    cnt += parseFloat(X) * 380000.0;
  } else {
    cnt += parseFloat(X);
  }
}
console.log(cnt);