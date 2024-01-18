const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const K = parseInt(input[0], 10);
const [A, B] = (input[1].split(" ")).map(x => parseInt(x, 10));
let flag = false;
for (let i = A; i < B + 1; i++) {
  if (i % K === 0) {
    flag = true;
    break;
  }
}
if (flag) {
  console.log("OK");
} else {
  console.log("NG");
}