const A = new Set(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[1].split(" ").map(x => parseInt(x, 10)));
for (let i = 0; i < 2001; i++) {
  if (!A.has(i)) {
    console.log(i);
    break;
  }
}