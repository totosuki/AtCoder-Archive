const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (2 ** N > N ** 2) {
  console.log("Yes");
} else {
  console.log("No");
}