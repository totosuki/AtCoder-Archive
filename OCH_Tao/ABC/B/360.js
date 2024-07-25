const [S, T] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ");
for (let i = 1; i < S.length; i++) {
  for (let j = 0; j < i; j++) {
    let X = "";
    for (let k = j; k < S.length; k += i) {
      X += S[k];
    }
    if (T === X) {
      console.log("Yes");
      process.exit();
    }
  }
}
console.log("No");