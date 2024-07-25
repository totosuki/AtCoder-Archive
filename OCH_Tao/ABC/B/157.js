const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const A = [];
for (let i = 0; i < 3; i++) {
  A.push(input.shift().split(" ").map(x => parseInt(x, 10)));
}
input.shift();
const B = input.map(x => parseInt(x, 10));
let flag = true;
for (const i of A) {
  if (i.every(x => B.includes(x))) {
    console.log("Yes");
    flag = false;
    break;
  }
}
for (let i = 0; i < 3 && flag; i++) {
  if (B.includes(A[0][i]) && B.includes(A[1][i]) && B.includes(A[2][i])) {
    console.log("Yes");
    flag = false;
    break;
  }
}
if (B.includes(A[0][0]) && B.includes(A[1][1]) && B.includes(A[2][2]) && flag) {
  console.log("Yes");
  flag = false;
} else if (B.includes(A[0][2]) && B.includes(A[1][1]) && B.includes(A[2][0]) && flag) {
  console.log("Yes");
  flag = false;
} else if (flag) {
  console.log("No");
}