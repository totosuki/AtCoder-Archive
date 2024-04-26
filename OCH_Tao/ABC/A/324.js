const A = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[1].split(" ");
if (A.every(x => x === A[0])) {
  console.log("Yes");
} else {
  console.log("No");
}