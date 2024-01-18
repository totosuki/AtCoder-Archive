const N = BigInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]);
let x = (N - 1n).toString(5);
x = BigInt(x) * 2n;
x = x.toString(10).replace("n", "");
console.log(x);