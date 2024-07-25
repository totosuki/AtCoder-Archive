const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, M] = input[0].split(" ").map(x => parseInt(x, 10));
const A = input[1].split(" ").map(x => parseInt(x, 10));
const B = input[2].split(" ").map(x => parseInt(x, 10));
let cnt = 0;
A.sort((a, b) => a - b);
B.sort((a, b) => a - b);
for (const i of A) {
  for (let j = 0; j < B.length; j++) {
    if (i < B[j]) {
      continue;
    } else {
      cnt += i;
      B.splice(j, 1);
      break;
    }
  }
}
console.log(cnt > 0 ? cnt : -1);