let N = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim(), 10);
let i = 0;
while (N > 0) {
  i++;
  N -= i;
}
console.log(i);