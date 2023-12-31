const [A, B, X] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (A <= X && X <= A + B) {
  console.log("YES");
} else {
  console.log("NO");
}