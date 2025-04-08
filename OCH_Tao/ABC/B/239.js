const X = BigInt(require("fs").readFileSync("/dev/stdin", "utf8").trim());
console.log(X < 0n && X % 10n !== 0n ? (X / 10n - 1n).toString() : (X / 10n).toString());