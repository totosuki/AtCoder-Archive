const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const A = input[1].split(" ").map(x => parseInt(x, 10));
const B = input[3].split(" ").map(x => parseInt(x, 10));
const C = input[5].split(" ").map(x => parseInt(x, 10));
const X = input[7].split(" ").map(x => parseInt(x, 10));
let S = new Set();
for (const i of A) {
  for (const j of B) {
    for (const k of C) {
      S.add(i + j + k);
    }
  }
}
for (const i of X) {
  if (S.has(i)) {
    console.log("Yes");
  } else {
    console.log("No");
  }
}