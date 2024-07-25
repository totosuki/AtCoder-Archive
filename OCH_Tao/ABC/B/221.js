const [S, T] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
if (S === T) {
  console.log("Yes");
} else {
  let X = [...S];
  for (let i = 0; i < S.length - 1; i++) {
    [X[i], X[i + 1]] = [X[i + 1], X[i]];
    if (X.join("") === T) {
      console.log("Yes");
      process.exit();
    } else {
      [X[i], X[i + 1]] = [X[i + 1], X[i]];
    }
  }
  console.log("No");
}