const [A, B] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
const X = parseInt(A + B, 10);
if (Math.trunc(Math.sqrt(X)) ** 2 === X) {
  console.log("Yes");
} else {
  console.log("No");
}