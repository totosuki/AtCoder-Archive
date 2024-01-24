const [S, T] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
if (S < T) {
  console.log("Yes");
} else {
  console.log("No");
}