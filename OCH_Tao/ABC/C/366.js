const [, ...Q] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
let M = new Map();
for (const i of Q) {
  if (i[0] === "1") {
    const X = parseInt(i.split(" ")[1], 10);
    M.set(X, (M.get(X) ?? 0) + 1);
  } else if (i[0] === "2") {
    const X = parseInt(i.split(" ")[1], 10);
    M.set(X, M.get(X) - 1);
    if (M.get(X) === 0) {
      M.delete(X);
    }
  } else {
    console.log(M.size);
  }
}