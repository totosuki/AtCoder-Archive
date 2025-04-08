const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = parseInt(input.shift(), 10);
let ans = [];
const roll = (l) => {
  let tmp = [];
  for (let i = 0; i < N; i++) {
    tmp.push(l.slice(i) + l.slice(0, i));
  }
  return tmp.concat(tmp.map(x => [...x].reverse().join("")));
};
for (const i of input) {
  ans.push(...roll(i));
}
for (let i = 0; i < N; i++) {
  const X = input.map(x => x[i]).join("");
  ans.push(...roll(X));
}
const index = roll([...new Array(N).keys()].join(""));
for (const i of index) {
  X = "";
  Y = "";
  for (let j = 0; j < N; j++) {
    X += input[j][i[j]];
  }
  for (let j = 0; j < N; j++) {
    Y += input[N - j - 1][i[j]];
  }
  ans.push(...roll(X));
  ans.push(...roll(Y));
}
console.log(Math.max(...ans.map(x => parseInt(x, 10))));