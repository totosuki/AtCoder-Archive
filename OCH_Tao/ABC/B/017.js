const X = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
let s = X.replaceAll("ch", "").replaceAll("o", "").replaceAll("k", "").replaceAll("u", "");
if (s) {
  console.log("NO");
} else {
  console.log("YES");
}