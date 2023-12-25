const N = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (N.includes("9")) {
  console.log("Yes");
} else {
  console.log("No");
}