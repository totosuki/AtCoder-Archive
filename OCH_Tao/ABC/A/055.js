const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
const x = N * 800;
const y = Math.trunc(N / 15) * 200;
console.log(x - y);