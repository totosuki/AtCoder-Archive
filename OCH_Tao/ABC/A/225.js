const S = [...(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]];
if (S[0] === S[1] && S[1] === S[2]) {
  console.log(1);
} else if (S[0] === S[1] || S[1] === S[2] || S[2] === S[0]) {
  console.log(3);
} else {
  console.log(6);
}