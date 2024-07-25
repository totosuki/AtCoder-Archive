const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const A = input[1].split(" ").map(x => parseInt(x, 10));
const B = input[2].split(" ").map(x => parseInt(x, 10));
const C = A.concat(B);
let flag = false;
C.sort((a, b) => a - b);
for (const i of C) {
  if (A.includes(i)) {
    if (flag) {
      console.log("Yes");
      return false;
    } else {
      flag = true;
    }
  } else {
    flag = false;
  }
}
console.log("No");