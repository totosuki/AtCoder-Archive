const [h, m] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let n = h % 12;
let l = [];
l.push(6 * m);
l.push(30 * n + m / 2);
let x = Math.abs(l[0] - l[1]);
if (x <= 180) {
  console.log(x);
} else {
  console.log(360 - x);
}