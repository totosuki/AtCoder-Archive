const [A, B] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0].split(" ").map(x => parseInt(x, 10));
const X = new RegExp("^" + Math.min(A, B).toString(2) + "[01]{1}$");
if (X.test(Math.max(A, B).toString(2))) {
  console.log("Yes");
} else {
  console.log("No");
}