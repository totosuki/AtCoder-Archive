const S = [...require("fs").readFileSync("/dev/stdin", "utf8").trim()];
S.sort();
console.log(S.join(""));