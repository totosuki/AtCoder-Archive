const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const S = input[0];
const T = parseInt(input[1], 10);
let x = 0;
let y = 0;
let cnt = 0;
for (let i = 0; i < S.length; i++) {
  if (S[i] === "L") {
    x--;
  } else if (S[i] === "R") {
    x++;
  } else if (S[i] === "U") {
    y++;
  } else if (S[i] === "D") {
    y--;
  } else {
    cnt++;
  }
}
let N = Math.abs(x) + Math.abs(y);
if (T === 1) {
  console.log(N + cnt);
} else {
  if (N > cnt) {
    console.log(N - cnt);
  } else {
    while (cnt > 0) {
      if (N > 0) {
        N--;
        cnt--;
      } else {
        N++;
        cnt--;
      }
    }
    console.log(N);
  }
}