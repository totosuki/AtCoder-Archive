const H = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[1].split(" ").map(x => parseInt(x, 10));
console.log(H.indexOf(Math.max(...H)) + 1);