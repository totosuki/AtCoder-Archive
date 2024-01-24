const [S, T, X] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (S < T) {
  if (S <= X && X < T) {
    console.log("Yes");
  } else {
    console.log("No");
  }
} else {
  if (S <= X || X < T) {
    console.log("Yes");
  } else {
    console.log("No");
  }
}