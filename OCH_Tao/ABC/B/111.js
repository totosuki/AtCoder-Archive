const N = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0], 10);
console.log(111 * Math.ceil(N / 111));