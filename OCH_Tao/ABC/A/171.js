const A = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (/[A-Z]/.test(A)) {
  console.log("A");
} else {
  console.log("a");
}