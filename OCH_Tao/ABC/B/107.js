const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [H, W] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
let A = [];
for (const a of input) {
  A.push([...a]);
}
let A1 = [];
for (const a of A) {
  if (a.some(x => x === "#")) {
    A1.push(a);
  }
}
let cnt = [];
for (let i = 0; i < W; i++) {
  let flag = true;
  for (const a of A1) {
    if (a[i] === "#") {
      flag = false;
      break;
    }
  }
  if (flag) {
    cnt.push(i);
  }
}
let A2 = [];
for (const a of A1) {
  let X = [];
  for (let i = 0; i < W; i++) {
    if (cnt.includes(i)) {
      continue;
    }
    X.push(a[i]);
  }
  A2.push(X);
}
for (const X of A2) {
  console.log(X.join(""));
}