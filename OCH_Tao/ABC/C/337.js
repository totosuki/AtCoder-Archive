//未AC
const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
const A = (input[1].split(" ")).map(x => parseInt(x, 10));
let l = [A.indexOf(-1) + 1];
for (let i = 0; i < N - 1; i++) {
  let x = l[i];
  l.push(A.indexOf(x) + 1);
}
console.log(l.join(" "));