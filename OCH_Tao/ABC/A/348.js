const N = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0], 10);
let L = [];
for (let i = 1; i < N + 1; i++) {
  L.push(i % 3 === 0 ? "x" : "o");
}
console.log(L.join(""));