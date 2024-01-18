const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (S[0] === S[1] && S[1] === S[2]) {
  console.log("No");
} else {
  console.log("Yes");
}