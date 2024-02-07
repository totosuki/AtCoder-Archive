const [S, input] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [A, B] = (input.split(" ")).map(x => parseInt(x, 10));
let l = [];
l.push(S.slice(0, A - 1));
l.push(S.slice(B - 1, B));
l.push(S.slice(A, B - 1));
l.push(S.slice(A - 1, A));
l.push(S.slice(B));
console.log(l.join(""));