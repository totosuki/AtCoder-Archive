const [A, B, K] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let l = [];
for (let i = A; i < A + K; i++) {
  l.push(i);
}
for (let i = B; i > B - K; i--) {
  l.push(i);
}
l = [...new Set(l)];
l = l.filter(x => A <= x && x <= B);
l.sort((a, b) => a - b);
console.log(l.join("\n"));