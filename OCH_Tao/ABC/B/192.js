const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0];
for (let i = 0; i < S.length; i++) {
  if (i % 2 === 0) {
    if (S[i] !== S[i].toLowerCase()) {
      console.log("No");
      return false;
    }
  } else {
    if (S[i] !== S[i].toUpperCase()) {
      console.log("No");
      return false;
    }
  }
}
console.log("Yes");