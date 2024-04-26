const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [N, X] = (input[0].split(" ")).map(x => parseInt(x, 10));
const L = (input[1].split(" ")).map(x => parseInt(x, 10));
let tmp = [0];
for (const i of L) {
  tmp.push(tmp[tmp.length - 1] + i);
}
console.log((tmp.filter(x => x <= X)).length);