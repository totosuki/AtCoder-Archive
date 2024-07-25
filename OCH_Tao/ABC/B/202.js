const S = [...require("fs").readFileSync("/dev/stdin", "utf8").trim()].reverse();
for (const i of S) {
  process.stdout.write(i === "6" ? "9" : i === "9" ? "6" : i);
}
console.log();