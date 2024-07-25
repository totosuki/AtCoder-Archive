const X = BigInt(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0]);
let N = 100n;
let i = 0;
while (N < X) {
  i++;
  N += (N / 100n);
}
console.log(i);