let [, ...S] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
S.reverse();
const X = Math.max(...S.map(x => x.length));
S = S.map(x => x.padEnd(X, "*"));
for (let i = 0; i < X; i++) {
  console.log(S.map(x => x[i]).join("").replace(/\*+$/, ""));
}