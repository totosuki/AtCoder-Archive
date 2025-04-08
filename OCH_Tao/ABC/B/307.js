const [N, ...S] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
for (let i = 0; i < parseInt(N); i++) {
  for (let j = 0; j < parseInt(N); j++) {
    if (i === j) {
      continue;
    }
    const X = S[i] + S[j];
    if (X === [...X].reverse().join("")) {
      console.log("Yes");
      process.exit();
    }
  }
}
console.log("No");