const P = [0, 0].concat(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(x => parseInt(x, 10)));
let i = P.length - 1;
let cnt = 0;
while (i !== 1) {
  cnt++;
  i = P[i];
}
console.log(cnt);