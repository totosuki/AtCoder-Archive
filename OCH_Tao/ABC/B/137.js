const [K, X] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
for (let i = X - K + 1; i < X + K; i++) {
  process.stdout.write(String(i) + " ");
  if (i === X + K - 1) {
    process.stdout.write("\n");
  }
}