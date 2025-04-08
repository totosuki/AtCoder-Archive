const [a, b, d] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
const D = d * (Math.PI / 180);
console.log(a * Math.cos(D) - b * Math.sin(D), a * Math.sin(D) + b * Math.cos(D));