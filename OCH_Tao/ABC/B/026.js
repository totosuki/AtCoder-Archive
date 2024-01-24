let R = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
const N = R.shift();
R.sort((a, b) => b - a);
let x = 0;
for (let i = 0; i < N; i++) {
  if (i % 2 === 0) {
    x += R[i] ** 2;
  } else {
    x -= R[i] ** 2;
  }
}
console.log(x * Math.PI);