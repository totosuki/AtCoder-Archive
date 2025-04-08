const S = [...require("fs").readFileSync("/dev/stdin", "utf8").trim()].map(x => Boolean(parseInt(x, 10)));
const T = [[0, 6], [0, 3], [0, 1, 7], [0, 4], [0, 2, 8], [0, 5], [0, 9]];
let X = [];
for (const i of T) {
  X.push((i.map(x => S[x])).some(x => x));
}
for (let i = 0; i < 5; i++) {
  for (let j = i + 2; j < 7; j++) {
    if (X[i] && X[j] && !(X.slice(i + 1, j).every(x => x))) {
      console.log("Yes");
      process.exit();
    }
  }
}
console.log("No");