const [N, K, A] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let x = (K + A - 1) % N;
if (x === 0) {
  console.log(N);
} else {
  console.log(x);
}