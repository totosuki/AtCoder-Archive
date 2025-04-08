const [N, A, B] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
for (let i = 0; i < N * A; i++) {
  for (let j = 0; j < N; j++) {
    if (Math.floor(i / A) % 2 === 0) {
      if (j % 2 === 0) {
        process.stdout.write(".".repeat(B));
      } else {
        process.stdout.write("#".repeat(B));
      }
    } else {
      if (j % 2 === 0) {
        process.stdout.write("#".repeat(B));
      } else {
        process.stdout.write(".".repeat(B));
      }
    }
  }
  console.log();
}