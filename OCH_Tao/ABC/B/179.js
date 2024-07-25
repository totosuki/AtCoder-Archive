const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
input.shift();
let cnt = 0;
for (const i of input) {
  const [X, Y] = i.split(" ");
  if (X === Y) {
    cnt++;
  } else {
    cnt = 0;
  }
  if (cnt === 3) {
    console.log("Yes");
    return false;
  }
}
console.log("No");