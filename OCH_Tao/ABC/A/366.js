const [N, T, A] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
console.log(N / 2 < T || N / 2 < A ? "Yes" : "No");