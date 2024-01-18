const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (S[2] === S[3] && S[4] === S[5]) {
  console.log("Yes");
} else {
  console.log("No");
}