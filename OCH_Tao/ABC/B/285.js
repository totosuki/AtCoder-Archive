const [N, S] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
for (let i = 1; i < parseInt(N, 10); i++) {
  for (let j = 0; j < parseInt(N, 10) - i; j++) {
    if (S[j] === S[j + i]) {
      console.log(j);
      break;
    } else if (j === parseInt(N, 10) - i - 1) {
      console.log(parseInt(N, 10) - i);
    }
  }
}