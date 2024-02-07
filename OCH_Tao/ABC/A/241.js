const A = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let x = 0;
for (let i = 0; i < 3; i++) {
  x = A[x];
}
console.log(x);