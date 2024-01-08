const [S, T] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
console.log(T + S);