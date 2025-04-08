const C = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [H, W] = C.shift().split(" ").map(x => parseInt(x, 10));
let [Si, Sj] = C.shift().split(" ").map(x => parseInt(x, 10) - 1);
const X = [...C.pop()];
for (const i of X) {
  if (i === "U") {
    if (Si !== 0 && C[Si - 1][Sj] === ".") {
      Si -= 1;
    }
  } else if (i === "D") {
    if (Si !== H - 1 && C[Si + 1][Sj] === ".") {
      Si += 1;
    }
  } else if (i === "L") {
    if (Sj !== 0 && C[Si][Sj - 1] === ".") {
      Sj -= 1;
    }
  } else {
    if (Sj !== W - 1 && C[Si][Sj + 1] === ".") {
      Sj += 1;
    }
  }
}
console.log(Si + 1, Sj + 1);