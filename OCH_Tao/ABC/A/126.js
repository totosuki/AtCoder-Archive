const [input, S] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [N, K] = (input.split(" ")).map(x => parseInt(x, 10));
const X = S.slice(0, K - 1);
const Y = S.slice(K - 1, K);
const Z = S.slice(K);
console.log(X + Y.toLowerCase() + Z);