const [X, Y] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0].split(" ").map(x => parseInt(x, 10));
let L = [];
for (let i = 0; i < X + 1; i++) {
  L.push(2 * i + 4 * (X - i));
}
console.log(L.includes(Y) ? "Yes" : "No");