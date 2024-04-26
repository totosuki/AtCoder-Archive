const [N, S] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
let flag = true;
for (let i = 0; i < parseInt(N, 10) - 1; i++) {
  if (S[i] === S[i + 1]) {
    flag = false;
    break;
  }
}
if (flag) {
  console.log("Yes");
} else {
  console.log("No");
}