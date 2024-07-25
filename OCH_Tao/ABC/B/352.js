const [S, T] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
let cnt = 0;
let L = [];
for (const i of [...S]) {
  let X = T.indexOf(i, cnt) + 1;
  L.push(X);
  cnt = X;
}
console.log(L.join(" "));