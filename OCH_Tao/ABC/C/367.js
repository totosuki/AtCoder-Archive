const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, K] = input[0].split(" ").map(x => parseInt(x, 10));
const R = input[1].split(" ").map(x => parseInt(x, 10));
let ans = [];
let L = new Array(N).fill(0);
const fn = (lv) => {
  if (lv === N) {
    let S = 0;
    for (let i = 0; i < N; i++) {
      S += L[i];
    } if (S % K === 0) {
      ans.push(L.join(" "));
    }
  }
  for (let i = 1; i < R[lv] + 1; i++) {
    L[lv] = i;
    fn(lv + 1);
  }
};
fn(0);
console.log(ans.join("\n"));