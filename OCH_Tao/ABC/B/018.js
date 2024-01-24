const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
let S = [...(input.shift())];
const N = parseInt(input.shift(), 10);
for (let i = 0; i < N; i++) {
  let [l, r] = (input[i].split(" ")).map(x => parseInt(x, 10));
  let x = S.splice(l - 1, r - l + 1);
  x.reverse()
  S.splice(l - 1, 0, ...x);
}
console.log(S.join(""));