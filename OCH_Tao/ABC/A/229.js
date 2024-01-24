const [S1, S2] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
if ((S1 == "#." && S2 == ".#") || (S1 == ".#" && S2 == "#.")) {
  console.log("No");
} else {
  console.log("Yes");
}