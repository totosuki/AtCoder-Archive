const [N, A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let cnt = 0;
for (let i = 1; i < N + 1; i++) {
  let x = ([...String(i)].map(x => parseInt(x, 10))).reduce((a, b) => a + b);
  if (A <= x && x <= B) {
    cnt += i;
  }
}
console.log(cnt);