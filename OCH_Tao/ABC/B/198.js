const N = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0];
for (let i = 0; i < 10; i++) {
  const S = "0".repeat(i) + N;
  if (S === [...S].reverse().join("")) {
    console.log("Yes");
    return false;
  }
}
console.log("No");