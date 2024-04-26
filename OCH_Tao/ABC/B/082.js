const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
let S = [...input[0]];
let T = [...input[1]];
S.sort();
T.sort();
T.reverse();
if (S < T) {
  console.log("Yes");
} else {
  console.log("No");
}