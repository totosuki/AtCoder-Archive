const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const A = input[1].split(" ").map(x => parseInt(x, 10));
const B = input[2].split(" ").map(x => parseInt(x, 10));
const C = A.reduce((x, y) => x.set(y, (x.get(y) ?? 0) + 1), new Map());
for (const i of B) {
  if (!C.has(i) || C.get(i) === 0) {
    console.log("No");
    process.exit();
  } else {
    C.set(i, C.get(i) - 1);
  }
}
console.log("Yes");