const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, T] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
let cnt = [];
for (const X of input) {
  const [c, t] = (X.split(" ")).map(x => parseInt(x, 10));
  if (t <= T) {
    cnt.push(c);
  }
}
if (cnt.length === 0) {
  console.log("TLE");
} else {
  console.log(Math.min(...cnt));
}