const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift(), 10);
let S = [];
let T = [];
for (const i of input) {
  const [x, y] = i.split(" ");
  S.push(x);
  T.push(y);
}
let Flag = true;
for (let i = 0; i < N; i++) {
  let SFlag = true;
  for (let j = 0; j < N; j++) {
    if (i === j) {
      continue;
    } else if (S[i] === S[j] || S[i] === T[j]) {
      SFlag = false;
      break;
    }
  }
  let TFlag = true;
  for (let j = 0; j < N; j++) {
    if (i === j) {
      continue;
    } else if (T[i] === S[j] || T[i] === T[j]) {
      TFlag = false;
      break;
    }
  }
  if (!SFlag && !TFlag) {
    Flag = false;
    break;
  }
}
if (Flag) {
  console.log("Yes");
} else {
  console.log("No");
}