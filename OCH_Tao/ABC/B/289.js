const [[N,], [...A]] = require("fs").readFileSync("/dev/stdin", "utf8").split("\n").map(x => x.split(" ").map(y => parseInt(y, 10)));
let L = [];
let tmp = 0;
for (let i = 1; i < N; i++) {
  if (!A.includes(i)) {
    L = L.concat([...Array(i - tmp).keys()].map(x => x + tmp + 1).reverse());
    tmp = i;
  }
}
L = L.concat([...Array(N - tmp).keys()].map(x => x + tmp + 1).reverse());
console.log(...L);