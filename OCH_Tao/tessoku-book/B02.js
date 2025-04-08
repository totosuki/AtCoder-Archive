const [A, B] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
for (let i = A; i < B + 1; i++) {
  if (100 % i === 0) {
    console.log("Yes");
    process.exit();
  }
}
console.log("No");