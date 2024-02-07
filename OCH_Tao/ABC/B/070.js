const [A, B, C, D] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
console.log(Math.max(Math.min(B, D) - Math.max(A, C), 0));