const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N,] = input.shift().split(" ").map(x => parseInt(x, 10));
const A = input.map(x => x.split(" ").map(y => parseInt(y, 10)));
let ans = 0;
for (let i = 1; i < N + 1; i++) {
  for (let j = i + 1; j < N + 1; j++) {
    let flag = false;
    check: {
      for (const x of A) {
        for (let k = 0; k < N - 1; k++) {
          if ((x[k] === i && x[k + 1] === j) || (x[k] === j && x[k + 1] === i)) {
            flag = true;
            break check;
          }
        }
      }
    }
    if (!flag) {
      ans++;
    }
  }
}
console.log(ans);