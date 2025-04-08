const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [L, R] = input[0].split(" ").map(x => parseInt(x, 10) - 1);
const S = input[1];
let ans = [];
ans.push(S.slice(0, L));
let rvs = S.slice(L, R + 1);
ans.push([...rvs].reverse().join(""));
ans.push(S.slice(R + 1));
console.log(ans.join(""));