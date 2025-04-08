const [, ...A] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n").map(x => x.split(" ").map(y => parseInt(y, 10)));
let ans = [];
for (const i of A) {
  ans.push(i.map(x => x === 0 ? "." : String.fromCharCode(64 + x)).join(""));
}
console.log(ans.join("\n"));