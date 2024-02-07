const [K, S] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let cnt = 0;
for (let x = 0; x <= K; x++) {
  for (let y = 0; y <= K; y++) {
    if (0 <= S - x - y && S - x - y <= K) {
      cnt++;
    }
  }
}
console.log(cnt);