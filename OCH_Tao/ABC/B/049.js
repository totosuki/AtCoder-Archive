const C = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [H, W] = (C.shift().split(" ")).map(x => parseInt(x, 10));
for (let i = 0; i < H; i++) {
  console.log(C[i]);
  console.log(C[i]);
}