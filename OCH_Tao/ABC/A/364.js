const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
input.shift();
let cnt = false;
let ans = false;
for (const i of input) {
  if (ans) {
    console.log("No");
    process.exit();
  }
  else if (cnt && i === "sweet") {
    ans = true;
  } else if (i === "sweet") {
    cnt = true;
  } else {
    cnt = false;
  }
}
console.log("Yes");