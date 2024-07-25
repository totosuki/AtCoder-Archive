const [S, T] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[1].split(" ");
for (let i = 0; i < S.length; i++) {
  process.stdout.write(S[i]);
  process.stdout.write(T[i]);
}
console.log();