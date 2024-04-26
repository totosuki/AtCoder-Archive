const N = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0], 10);
let S = new Set();
for (let i = 0; i < 26; i++) {
  for (let j = 0; j < 15; j++) {
    S.add(4 * i + 7 * j);
  }
}
if (S.has(N)) {
  console.log("Yes");
} else {
  console.log("No");
}