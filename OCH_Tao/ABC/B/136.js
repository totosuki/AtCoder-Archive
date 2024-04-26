const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
let cnt = 0;
for (let i = 1; i < N + 1; i++) {
  if (String(i).length % 2 === 1) {
    cnt++;
  }
}
console.log(cnt);