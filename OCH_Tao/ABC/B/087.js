const [A, B, C, X] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
let l = [];
for (let i = 0; i < A + 1; i++) {
  for (let j = 0; j < B + 1; j++) {
    for (let k = 0; k < C + 1; k++) {
      l.push(500 * i + 100 * j + 50 * k);
    }
  }
}
console.log((l.filter(x => x === X)).length);