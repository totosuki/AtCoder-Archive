const A = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
A.sort((a, b) => a - b);
if (A[2] - A[1] === A[1] - A[0]) {
  console.log("Yes");
} else {
  console.log("No");
}