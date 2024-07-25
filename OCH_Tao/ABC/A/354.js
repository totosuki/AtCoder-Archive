const H = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0], 10);
let i = 0;
let cnt = 0;
while (true) {
  cnt += 2 ** i;
  i++;
  if (H < cnt) {
    console.log(i);
    break;
  }
}