const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const xy = input[0].split(" ");
const X = parseInt(xy[0], 10);
const Y = parseInt(xy[1], 10);
console.log(Math.trunc(Y / X));