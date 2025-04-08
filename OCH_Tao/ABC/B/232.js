const [S, T] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n").map(x => [...x].map(y => y.charCodeAt(0) - 97));
const diff = S[0] - T[0];
for (let i = 0; i < S.length; i++) {
  if ((26 + S[i] - diff) % 26 !== T[i]) {
    console.log("No");
    process.exit();
  }
}
console.log("Yes");