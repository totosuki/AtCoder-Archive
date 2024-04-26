const [, ...S] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
let cnt = 0;
for (const i of [...S.join("")]) {
  if (i === "#") {
    cnt++;
  }
}
console.log(cnt);