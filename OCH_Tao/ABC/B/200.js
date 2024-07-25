let [N, K] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0].split(" ").map(x => parseInt(x, 10));
for (let i = 0; i < K; i++) {
  if (N % 200 === 0) {
    N /= 200;
  } else {
    N = parseInt(N.toString() + "200", 10);
  }
}
console.log(N);