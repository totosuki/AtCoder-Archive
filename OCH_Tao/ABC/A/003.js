const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const N = parseInt(input, 10);
let money = 0;
for (let i = 1; i < N + 1; i++) {
  money += i * 10000;
}
money /= N;
console.log(money);