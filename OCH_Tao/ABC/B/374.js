const [S, T] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
if (S === T) {
  console.log(0);
} else {
  for (let i = 0; i < Math.max(S.length, T.length); i++) {
    try {
      if (S[i] !== T[i]) {
        console.log(i + 1);
        break;
      }
    } catch {
      console.log(i + 1);
      break;
    }
  }
}