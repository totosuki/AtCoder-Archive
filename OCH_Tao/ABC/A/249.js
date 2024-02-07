const [A, B, C, D, E, F, X] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let Taka = 0;
let Ao = 0;
for (let i = 0; i < X; i++) {
  if (i % (A + C) < A) {
    Taka += B;
  }
  if (i % (D + F) < D) {
    Ao += E;
  }
}
if (Taka === Ao) {
  console.log("Draw");
} else if (Taka > Ao) {
  console.log("Takahashi");
} else {
  console.log("Aoki");
}