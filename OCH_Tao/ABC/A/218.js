const [N, S] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const X = parseInt(N, 10);
if (S[X - 1] === "o") {
  console.log("Yes");
} else {
  console.log("No");
}