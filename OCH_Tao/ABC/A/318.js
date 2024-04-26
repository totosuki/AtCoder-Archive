const [N, M, P] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ").map(x => parseInt(x, 10));
let tmp = N - M;
let cnt = 0;
while (tmp >= 0) {
  cnt++;
  tmp -= P;
}
console.log(cnt);