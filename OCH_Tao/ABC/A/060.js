const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
if ((S[0])[S[0].length - 1] === (S[1])[0] && (S[1])[S[1].length - 1] === (S[2])[0]) {
  console.log("YES");
} else {
  console.log("NO");
}