let [X, Y, N] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ").map(x => parseInt(x, 10));
if (3 * X < Y) {
  console.log(X * N);
} else {
  let cnt = 0;
  while (N > 2) {
    cnt += Y;
    N -= 3;
  }
  console.log(cnt + N * X);
}