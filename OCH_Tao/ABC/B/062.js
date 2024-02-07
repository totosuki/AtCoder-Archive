const A = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [H, W] = ((A.shift()).split(" ")).map(x => parseInt(x, 10));
console.log("#".repeat(W + 2));
for (let i = 0; i < H; i++) {
  console.log(`#${A[i]}#`);
}
console.log("#".repeat(W + 2));