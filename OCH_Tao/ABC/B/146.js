const X = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const [N, S] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const Y = X.slice(parseInt(N, 10)) + X.slice(0, parseInt(N, 10));
let L = [];
for (let i = 0; i < S.length; i++) {
  L.push(Y[X.indexOf(S[i])]);
}
console.log(L.join(""));