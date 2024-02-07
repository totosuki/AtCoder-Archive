const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [L, H] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
const N = parseInt((input.shift()), 10);
const A = input.map(x => parseInt(x, 10));
for (let i = 0; i < N; i++) {
  let x = A[i];
  if (L <= x && x <= H) {
    console.log(0);
  } else if (H < x) {
    console.log(-1);
  } else {
    console.log(L - x);
  }
}