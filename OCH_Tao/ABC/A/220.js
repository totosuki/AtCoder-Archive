const [A, B, C] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let flag = true;
for (let i = A; i < B + 1; i++) {
  if (i % C === 0) {
    console.log(i);
    flag = false;
    break;
  }
}
if (flag) {
  console.log(-1);
}