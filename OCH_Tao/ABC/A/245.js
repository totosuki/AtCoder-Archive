const [A, B, C, D] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let flag;
if (A < C) {
  flag = true;
} else if (C < A) {
  flag = false;
} else {
  if (B <= D) {
    flag = true;
  } else {
    flag = false;
  }
}
if (flag) {
  console.log("Takahashi");
} else {
  console.log("Aoki");
}