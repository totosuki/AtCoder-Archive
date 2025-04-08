const H = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(x => parseInt(x, 10));
let T = 0;
for (const i of H) {
  T += Math.floor(i / 5) * 3;
  let M = i % 5;
  while (M > 0) {
    T++;
    if (T % 3 === 0) {
      M -= 3;
    } else {
      M--;
    }
  }
}
console.log(T);