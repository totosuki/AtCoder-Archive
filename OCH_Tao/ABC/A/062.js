const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
const A = [1, 3, 5, 7, 8, 10, 12];
const B = [4, 6, 9, 11];
const C = [2];
if (A.includes(input[0]) && A.includes(input[1])) {
  console.log("Yes");
} else if (B.includes(input[0]) && B.includes(input[1])) {
  console.log("Yes");
} else if (C.includes(input[0]) && C.includes(input[1])) {
  console.log("Yes");
} else {
  console.log("No");
}