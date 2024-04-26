const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [A, B] = (input[0].split(" ")).map(x => parseInt(x, 10));
const S = [...(input[1])];
const X = S.splice(A, 1);
if (X == "-") {
  if (!isNaN(S.join(""))) {
    console.log("Yes");
  } else {
    console.log("No");
  }
} else {
  console.log("No");
}