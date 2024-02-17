const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const N = parseInt(input[0], 10);
let A = (input[1].split(" ")).map(x => parseInt(x, 10));
let cnt = 0;
while (A.every(x => x % 2 === 0)) {
  A = A.map(x => x / 2);
  cnt++;
}
console.log(cnt);