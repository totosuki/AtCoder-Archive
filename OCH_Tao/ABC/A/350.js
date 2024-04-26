const S = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].slice(3));
console.log(S === 316 ? "No" : 0 < S && S < 350 ? "Yes" : "No");