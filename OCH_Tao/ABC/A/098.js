const [A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let l = [];
l.push(A + B);
l.push(A - B);
l.push(A * B + 0);
console.log(Math.max(...l));