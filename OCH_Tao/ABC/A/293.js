let S = [...(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]];
for (let i = 0; i < S.length / 2; i++) {
  [S[2 * i], S[2 * i + 1]] = [S[2 * i + 1], S[2 * i]];
}
console.log(S.join(""));