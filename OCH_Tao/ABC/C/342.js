const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input.shift(), 10);
let S = input.shift();
const Q = parseInt(input.shift(), 10);
/*
for (const X of input) {
  let [C, D] = X.split(" ")
  S = S.replaceAll(C, D);
}
console.log(S);
*/
let abc_to = "abcdefghijklmnopqrstuvwxyz"
const abc_from = "abcdefghijklmnopqrstuvwxyz"
for (const X of input) {
  let [C, D] = X.split(" ");
  abc_to = abc_to.replaceAll(C, D);
}
let l = [];
for (const X of [...S]) {
  let i = abc_from.indexOf(X);
  l.push(abc_to[i]);
}
console.log(l.join(""));