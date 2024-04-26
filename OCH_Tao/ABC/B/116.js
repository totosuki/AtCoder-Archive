const S = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0], 10);
const fn = n => {
  if (n % 2 === 0) {
    return n / 2;
  } else {
    return 3 * n + 1;
  }
}
let X = new Set();
X.add(S);
let cnt = 1;
let tmp = S;
while (true) {
  cnt++;
  tmp = fn(tmp);
  if (X.has(tmp)) {
    console.log(cnt);
    break;
  } else {
    X.add(tmp);
  }
}