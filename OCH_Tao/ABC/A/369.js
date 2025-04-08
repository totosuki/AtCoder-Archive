const [A, B] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
console.log(A === B ? 1 : (A + B) % 2 === 0 ? 3 : 2);