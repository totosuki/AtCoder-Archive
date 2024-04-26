const [A, B] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ").map(x => parseInt(x, 10));
console.log(A + B === 0 ? 1 : 0);