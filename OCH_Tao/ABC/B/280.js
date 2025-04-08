const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(x => parseInt(x, 10));
let ans = [];
S.reduce((a, b) => { ans.push(b - a); return b; }, 0);
console.log(ans.join(" "));