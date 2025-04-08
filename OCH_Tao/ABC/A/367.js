const [A, B, C] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
if ((B <= A && A <= C) || (B > C && (B <= A || A <= C))) {
  console.log("No");
} else {
  console.log("Yes");
}