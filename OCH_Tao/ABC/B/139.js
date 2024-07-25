const [A, B] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ").map(x => parseInt(x, 10));
let cnt = 1;
let ans = 0;
while (cnt < B) {
  ans++;
  cnt += A - 1;
}
console.log(ans)