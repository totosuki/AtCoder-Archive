const N = [...require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0]].map(x => parseInt(x, 10));
console.log(N.reduce((a, b) => a + b, 0) % 9 === 0 ? "Yes" : "No");