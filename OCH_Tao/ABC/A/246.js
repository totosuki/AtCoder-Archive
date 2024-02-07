const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [x1, y1] = input[0].split(" ");
const [x2, y2] = input[1].split(" ");
const [x3, y3] = input[2].split(" ");
let l = [];
if (x1 === x2) {
  l.push(x3);
} else if (x2 === x3) {
  l.push(x1);
} else {
  l.push(x2);
}
if (y1 === y2) {
  l.push(y3);
} else if (y2 === y3) {
  l.push(y1);
} else {
  l.push(y2);
}
console.log(l.join(" "));