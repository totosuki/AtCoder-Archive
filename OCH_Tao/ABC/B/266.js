const N = BigInt(require("fs").readFileSync("/dev/stdin", "utf8").trim());
console.log((((N % 998244353n) + 998244353n) % 998244353n).toString());