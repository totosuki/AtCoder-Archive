const T = [...require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1]];
let ans = [0, 0];
let cnt = 0;
for (const i of T) {
  if (i === "R") {
    cnt++;
  } else {
    if (cnt % 4 === 0) {
      ans[0]++;
    } else if (cnt % 4 === 1) {
      ans[1]--;
    } else if (cnt % 4 === 2) {
      ans[0]--;
    } else {
      ans[1]++;
    }
  }
}
console.log(...ans);