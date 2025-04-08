const N = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim(), 10);
let ans = [[1]];
for (let i = 0; i < N - 1; i++) {
  let L = [1];
  for (let j = 0; j < i; j++) {
    L.push(ans[ans.length - 1][j] + ans[ans.length - 1][j + 1]);
  }
  L.push(1);
  ans.push(L);
}
console.log(ans.map(x => x.join(" ")).join("\n"));