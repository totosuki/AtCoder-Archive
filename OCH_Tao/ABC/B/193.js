const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n").slice(1);
let ans = [];
for (const i of input) {
  const [A, P, X] = i.split(" ").map(x => parseInt(x, 10));
  if (X - A > 0) {
    ans.push(P);
  }
}
console.log(ans.length > 0 ? Math.min(...ans) : -1);