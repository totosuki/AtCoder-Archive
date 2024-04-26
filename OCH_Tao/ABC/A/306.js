const S = [...(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[1]];
for (const i of S) {
  process.stdout.write(i.repeat(2));
}
process.stdout.write("\n");