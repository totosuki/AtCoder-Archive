const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
for (let i = 1; i < 8; i++) {
  if (N < 2 ** i) {
    console.log(2 ** (i - 1));
    break;
  }
}