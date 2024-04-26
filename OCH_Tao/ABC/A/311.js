const [N, S] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
let D = { "A": 0, "B": 0, "C": 0 };
for (let i = 0; i < parseInt(N, 10); i++) {
  D[S[i]] = D[S[i]] + 1;
  if (D["A"] > 0 && D["B"] > 0 && D["C"] > 0) {
    console.log(i + 1);
    break;
  }
}