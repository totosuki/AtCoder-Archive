const [, S] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
if (S.includes("o") && !S.includes("x")) {
  console.log("Yes");
} else {
  console.log("No");
}