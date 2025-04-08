const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [, W] = input.shift().split(" ").map(x => parseInt(x, 10));
const S = input.join("");
const X = S.indexOf("o");
const Y = S.lastIndexOf("o");
console.log(Math.abs(Math.floor(X / W) - Math.floor(Y / W)) + Math.abs(X % W - Y % W));