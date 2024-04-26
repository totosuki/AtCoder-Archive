const X = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
let L = [];
for (let i = 2; i < 10; i++) {
  for (let j = 1; j < 32; j++) {
    L.push(j ** i);
  }
}
L = [...new Set(L)];
L = L.filter(a => a <= X);
console.log(Math.max(...L));