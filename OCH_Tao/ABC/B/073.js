const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input.shift(), 10);
let cnt = 0;
for (let i = 0; i < N; i++) {
  let [l, r] = (input[i].split(" ")).map(x => parseInt(x, 10));
  cnt += r - l + 1;
}
console.log(cnt);