const [X, Y] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ").map(x => parseInt(x, 10));
console.log(-3 <= Y - X && Y - X <= 2 ? "Yes" : "No");