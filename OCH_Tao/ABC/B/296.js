const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
for (let i = 0; i < 8; i++) {
  if (S[i].includes("*")) {
    console.log(`${String.fromCharCode(S[i].indexOf("*") + 97)}${8 - i}`);
  }
}