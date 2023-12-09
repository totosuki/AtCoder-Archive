const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
let N = parseInt(input[0], 10);
console.log(N * 2);