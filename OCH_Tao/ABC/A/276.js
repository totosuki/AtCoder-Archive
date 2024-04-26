const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
const X = S.lastIndexOf("a");
if (X === -1) {
  console.log(X);
} else {
  console.log(X + 1);
}