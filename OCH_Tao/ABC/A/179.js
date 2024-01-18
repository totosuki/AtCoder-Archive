const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (S[S.length - 1] === "s") {
  console.log(S + "es");
} else {
  console.log(S + "s");
}