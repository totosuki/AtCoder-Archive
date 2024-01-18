const [N, M] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (N === M) {
  console.log("Yes");
} else {
  console.log("No");
}