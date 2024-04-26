const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, D] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
let X = [];
for (const i of input) {
  X.push((i.split(" ")).map(x => parseInt(x, 10)));
}
let cnt = 0;
for (let i = 0; i < N - 1; i++) {
  const A = X[i];
  for (let j = i + 1; j < N; j++) {
    const B = X[j];
    let tmp = 0;
    for (let k = 0; k < D; k++) {
      tmp += (A[k] - B[k]) ** 2;
    }
    tmp = Math.sqrt(tmp);
    if (tmp % 1 == 0) {
      cnt++;
    }
  }
}
console.log(cnt);