const [A, B, X] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(BigInt);
if (A % X === 0n) {
  console.log(((B / X) - (A / X) + 1n).toString());
} else {
  console.log(((B / X) - (A / X)).toString());
}