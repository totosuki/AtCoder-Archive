const N = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim(), 10);
for (let i = 0; i < N + 1; i++) {
  for (let j = 0; j < N + 1 - i; j++) {
    for (let k = 0; k < N + 1 - i - j; k++) {
      console.log(i, j, k);
    }
  }
}