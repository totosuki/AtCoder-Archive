const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [R, C] = input.shift().split(" ").map(x => parseInt(x, 10));
let B = [];
for (const i of input) {
  B.push([...i]);
}
for (let i = 0; i < R; i++) {
  for (let j = 0; j < C; j++) {
    if (/\d/.test(B[i][j])) {
      const N = parseInt(B[i][j], 10);
      for (let r = 0; r < R; r++) {
        for (let c = 0; c < C; c++) {
          if (Math.abs(r - i) + Math.abs(c - j) <= N && !/\d/.test(B[r][c])) {
            B[r][c] = ".";
          }
        }
      }
      B[i][j] = ".";
    }
  }
}
console.log(B.map(x => x.join("")).join("\n"));