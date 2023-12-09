const H = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const H1 = parseInt(H[0], 10);
const H2 = parseInt(H[1], 10);
let result = H1 - H2;
console.log(result);