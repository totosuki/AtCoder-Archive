const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const A = (input[0].split(" ")).map(x => parseInt(x, 10));
const B = (input[1].split(" ")).map(x => parseInt(x, 10));
let flag = true;
for (let i = 0; i < 2 && flag; i++) {
  for (let j = 0; j < 2 && flag; j++) {
    if (A[i] === B[j]) {
      console.log("YES");
      flag = false;
      break;
    }
  }
}
if (flag) {
  console.log("NO");
}