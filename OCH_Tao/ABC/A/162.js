const N = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (N.includes("7")) {
  console.log("Yes");
} else {
  console.log("No");
}