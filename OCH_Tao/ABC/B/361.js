const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [A, B, C, D, E, F] = input[0].split(" ").map(x => parseInt(x, 10));
const [G, H, I, J, K, L] = input[1].split(" ").map(x => parseInt(x, 10));
const f = (x1, x2, y1, y2) => { return !(x2 <= y1 || y2 <= x1); };
console.log(f(A, D, G, J) && f(B, E, H, K) && f(C, F, I, L) ? "Yes" : "No");