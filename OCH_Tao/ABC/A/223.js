const X = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (X === 0) {
  console.log("No");
} else if (X % 100 === 0) {
  console.log("Yes");
} else {
  console.log("No");
}