const [N, L, R] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0].split(" ").map(x => parseInt(x, 10));
let X = [...Array(N).keys()].map(x => x + 1);
let ans = [];
ans.push(...X.slice(0, L - 1));
let rvs = X.slice(L - 1, R);
rvs.reverse();
ans.push(...rvs);
ans.push(...X.slice(R));
console.log(ans.join(" "));