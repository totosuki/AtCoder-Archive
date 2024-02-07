const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (-(2 ** 31) <= N && N < 2 ** 31) {
  console.log("Yes");
} else {
  console.log("No");
}