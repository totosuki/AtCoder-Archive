const [, X, Y, Z] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ").map(x => parseInt(x, 10));
console.log(Math.min(X, Y) < Z && Z < Math.max(X, Y) ? "Yes" : "No");