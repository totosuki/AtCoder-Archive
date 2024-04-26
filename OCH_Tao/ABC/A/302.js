const [A, B] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ").map(BigInt);
console.log(((A + B - 1n) / B).toString());