const [N, ...S] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
let cnt = 0;
for (const i of S) {
  if (i === "For") {
    cnt++;
  }
}
if (Math.floor(parseInt(N, 10) / 2) < cnt) {
  console.log("Yes");
} else {
  console.log("No");
}