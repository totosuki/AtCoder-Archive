const [N, M] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let x = 0;
let y = 0;
if (N > 0) {
  x = Math.trunc((N * (N - 1)) / 2);
}
if (M > 0) {
  y = Math.trunc((M * (M - 1)) / 2);
}
console.log(x + y);