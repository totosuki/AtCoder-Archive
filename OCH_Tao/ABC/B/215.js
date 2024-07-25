const N = BigInt(require("fs").readFileSync("/dev/stdin", "utf8").trim());
console.log(N.toString(2).length - 1);