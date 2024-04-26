const [, ...X] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
for (const i of X) {
  const [A, B] = i.split(" ").map(x => parseInt(x, 10));
  console.log(A + B);
}