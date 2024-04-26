const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [, K] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ");
for (let i = 0; i < K; i++) {
  A.shift();
  A.push("0");
}
console.log(A.join(" "));