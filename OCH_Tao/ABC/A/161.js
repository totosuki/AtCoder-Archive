const [X, Y, Z] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
console.log(`${Z} ${X} ${Y}`);