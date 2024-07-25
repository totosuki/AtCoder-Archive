const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [R, G, B] = input[0].split(" ").map(x => parseInt(x, 10));
const C = input[1];
console.log(C === "Red" ? Math.min(G, B) : C === "Green" ? Math.min(B, R) : Math.min(R, G));