const A = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
A.sort((a, b) => a - b);
console.log((A[2] - A[1]) + (A[1] - A[0]));