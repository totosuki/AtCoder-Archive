const N = [...(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]].map(x => parseInt(x, 10));
let flag = true;
for (let i = 0; i < N.length - 1; i++) {
  if (N[i] <= N[i + 1]) {
    flag = false;
  }
}
if (flag) {
  console.log("Yes");
} else {
  console.log("No");
}