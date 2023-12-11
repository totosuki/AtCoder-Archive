const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const N = parseInt(input[0], 10);
console.log(Math.ceil(N / 2));