const N = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (N[0] === N[2]) {
  console.log("Yes");
} else {
  console.log("No");
}