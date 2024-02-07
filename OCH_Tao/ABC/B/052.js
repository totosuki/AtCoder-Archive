const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
const S = [...input[1]];
let l = [0];
for (let i = 0; i < N; i++) {
  if (S[i] === "I") {
    l.push(l[l.length - 1] + 1);
  } else {
    l.push(l[l.length - 1] - 1);
  }
}
console.log(Math.max(...l));