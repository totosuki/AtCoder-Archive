const [A, B, C] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let flag = false;
for (let i = 1; i < 1e3; i++) {
  if ((A * i) % B === C) {
    flag = true;
    break;
  }
}
if (flag) {
  console.log("YES");
} else {
  console.log("NO");
}