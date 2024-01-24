const [A, B] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
const X = parseInt(A + B, 10);
console.log(2 * X);