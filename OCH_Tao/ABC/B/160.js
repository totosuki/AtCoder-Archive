let X = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0], 10);
const cnt = Math.floor(X / 500) * 1000;
X = X % 500;
console.log(cnt + Math.floor(X / 5) * 5);