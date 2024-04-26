const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
let flag = true;
for (let i = 1; i < 16; i += 2) {
  if (S[i] === "1") {
    flag = false;
    break;
  }
}
if (flag) {
  console.log("Yes");
} else {
  console.log("No");
}