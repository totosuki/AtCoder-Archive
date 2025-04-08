let M = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim(), 10);
let L = [];
for (let i = 10; i > -1; i--) {
  while (M >= 3 ** i) {
    L.push(i);
    M -= 3 ** i;
  }
}
console.log(L.length);
console.log(...L);