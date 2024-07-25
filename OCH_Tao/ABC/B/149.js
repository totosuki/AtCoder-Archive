let [A, B, K] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ").map(x => parseInt(x, 10));
const X = Math.min(A, K);
A -= X;
K -= X;
const Y = Math.min(B, K);
B -= Y;
K -= Y;
console.log(`${A} ${B}`);