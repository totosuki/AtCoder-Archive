const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (S.length !== ([...new Set(S)].length)) {
  console.log("no");
} else {
  console.log("yes");
}