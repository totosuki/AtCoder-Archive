const A = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(x => parseInt(x, 10));
let ans = [];
for (let i = 2; i < 1001; i++) {
  ans.push(A.filter(x => x % i === 0).length);
}
console.log(ans.indexOf(Math.max(...ans)) + 2);