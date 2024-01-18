const [D, T, S] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (D / S <= T) {
  console.log("Yes");
} else {
  console.log("No");
}