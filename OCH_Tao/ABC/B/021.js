const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
const [A, B] = (input[1].split(" ")).map(x => parseInt(x, 10));
const K = parseInt(input[2], 10);
const P = (input[3].split(" ")).map(x => parseInt(x, 10));
P.push(A);
P.push(B);
const X = [...new Set(P)];
if (P.length !== X.length) {
  console.log("NO");
} else {
  console.log("YES");
}