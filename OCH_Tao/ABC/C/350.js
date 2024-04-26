const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
let A = input[1].split(" ").map(x => parseInt(x, 10));
let ans = [];
for (let i = 0; i < N; i++) {
  while (A[i] !== i + 1) {
    ans.push([i + 1, A[i]])
    let tmp = A[i] - 1;
    [A[i], A[tmp]] = [A[tmp], A[i]];
  }
}
console.log(ans.length)
for (const i of ans) {
  console.log(i.join(" "));
}