const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [H, W] = (input[0].split(" ")).map(x => parseInt(x, 10));
const [R, C] = (input[1].split(" ")).map(x => parseInt(x, 10));
let cnt = 0;
if (R != 1) {
  cnt++;
}
if (R != H) {
  cnt++;
}
if (C != 1) {
  cnt++;
}
if (C != W) {
  cnt++;
}
console.log(cnt);