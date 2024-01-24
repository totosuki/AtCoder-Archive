const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [N, A, B] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
let x = 0;
for (let i = 0; i < N; i++) {
  let SD = input[i].split(" ");
  let s = SD[0];
  let d = parseInt(SD[1], 10);
  if (A <= d && d <= B) {
    if (s === "East") {
      x += d;
    } else {
      x -= d;
    }
  } else if (d < A) {
    if (s === "East") {
      x += A;
    } else {
      x -= A;
    }
  } else {
    if (s === "East") {
      x += B;
    } else {
      x -= B;
    }
  }
}
if (x > 0) {
  console.log(`East ${x}`);
} else if (x === 0) {
  console.log(0);
} else {
  console.log(`West ${Math.abs(x)}`);
}