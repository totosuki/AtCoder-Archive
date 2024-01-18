const [S, T] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
if (S === T.slice(0, -1)) {
  console.log("Yes");
} else {
  console.log("No");
}