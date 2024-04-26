const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ").map(x => parseInt(x, 10));
let flag = true;
for (let i = 0; i < 7; i++) {
  if (S[i] > S[i + 1]) {
    flag = false;
    break;
  }
}
if (Math.min(...S) < 100 || Math.max(...S) > 675) {
  flag = false;
}
if (S.some(x => x % 25 !== 0)) {
  flag = false;
}
if (flag) {
  console.log("Yes");
} else {
  console.log("No");
}